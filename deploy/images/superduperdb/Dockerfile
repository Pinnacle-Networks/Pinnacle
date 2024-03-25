# syntax = docker/dockerfile:experimental

# ---------------
# Global Parameters
# ---------------
# BUILD_ENV choses whether to use local source (sandbox) or released wheel (pypi).
ARG BUILD_ENV=release
ARG REQUIREMENTS_FILE=deploy/testenv/optional_requirements.txt

# ---------------
# Configure Basic Template
# ---------------
# TODO make this configurable
FROM jupyterhub/k8s-singleuser-sample:3.1.0 as base

# Temporarily switch to the root for privileged operations.
# ---------------
USER root

# Install system packages
# ---------------
# TODO make this configurable
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y --no-install-recommends \
        # Required for downloading code/data from the internet \
        wget curl unzip git \
        # DevOps
        vim procps make \
        # Required by OpenCV
        libglib2.0-0 libgl1-mesa-glx \
        # Required for PostgreSQL \
        libpq-dev \
        # Required for rest server \
        libmagic1 \
        # Required for Llama.cpp
        build-essential \
  # Purge apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


# Replace the default Jupyter user with a SuperDuper user
# ---------------
ENV NB_USER=pinnacle \
    NB_UID=1000 \
    HOME=/home/pinnacle

RUN deluser jovyan && rm -rf /home/jovyan \
    && adduser \
        --disabled-password \
        --gecos "SuperDuper User" \
        --uid ${NB_UID} \
        --home ${HOME} \
        --force-badname \
        ${NB_USER}


# Switch to SuperDuper user
# ---------------
WORKDIR ${HOME}
USER ${NB_USER}
ENV PATH="${HOME}/.local/bin:$PATH"


# Install common dependencies
# ---------------
RUN python -m pip install setuptools pip
RUN --mount=type=cache,uid=1000,target=/home/pinnacle/.cache/pip python -m pip install --user \
    # JupyterLab extensions \
    theme-darcula \
    ipywidgets \
    jupyterlab-lsp \
    'python-lsp-server[all]'


# Install Jupyterlab extensions
# ---------------
COPY --chown=pinnacle ./deploy/images/pinnacledb/labextensions/@pinnacledb ${HOME}/.local/share/jupyter/labextensions/@pinnacledb
COPY --chown=pinnacle ./deploy/images/pinnacledb/apputils-extension/themes.jupyterlab-settings ${HOME}/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

# Volumes
# ---------------
VOLUME /artifacts

# Runtime Configuration
# ---------------

# Don't write .pyc files on the import of source modules.
ENV PYTHONDONTWRITEBYTECODE 1
# Set python cache directory
ENV PYTHONPYCACHEPREFIX "$HOME/.cache/cpython/"

# -------------------------------
# Build Sandbox (Development)
# -------------------------------
FROM base AS build_sandbox

# Install the requirements. To be used in conjuction with "make testenv_init" for development.
ONBUILD ARG REQUIREMENTS_FILE
ONBUILD USER pinnacle
ONBUILD COPY --chown=pinnacle ./pyproject.toml ${HOME}/pinnacledb/pyproject.toml
ONBUILD COPY --chown=pinnacle ./deploy/testenv/requirements.txt ${HOME}/pinnacledb/requirements.txt
ONBUILD COPY --chown=pinnacle ./Makefile ${HOME}/pinnacledb/Makefile
ONBUILD COPY --chown=pinnacle ./${REQUIREMENTS_FILE} ${HOME}/pinnacledb/optional_requirements.txt
ONBUILD WORKDIR ${HOME}/pinnacledb
ONBUILD RUN --mount=type=cache,uid=1000,target=/home/pinnacle/.cache/pip python -m pip install --user -r requirements.txt
ONBUILD RUN --mount=type=cache,uid=1000,target=/home/pinnacle/.cache/pip python -m pip install --user -r ./optional_requirements.txt
ONBUILD RUN make install-devkit


# -------------------------------
# Build Nightly (Pre-Release)
# -------------------------------
FROM base AS build_nightly

# Install the latest commit of the main branch in GitHub.
ONBUILD WORKDIR ${HOME}/pinnacledb
ONBUILD RUN git clone -b main --single-branch  https://github.com/SuperDuperDB/pinnacledb.git .
ONBUILD RUN python -m pip install --user . \
    # Install optional dependencies for testing
    && python -m pip install --user -r deploy/testenv/optional_requirements.txt \
    # Purge pip cache to reduce image size.
    && pip cache purge


# -------------------------------
# Build Release (Production)
# -------------------------------
FROM base AS build_release

# Install the latest release from pypi, including code from the GitHub branch of the release.
# TODO: to be updated when we create the release branch.
ONBUILD COPY --chown=pinnacle ${PWD}/examples ./examples
ONBUILD RUN python -m pip install --user pinnacledb \
    # Purge pip cache to reduce image size.
    && pip cache purge
ONBUILD WORKDIR ${HOME}/examples



# ---------------
# Select Build
# ---------------
FROM build_${BUILD_ENV}
EXPOSE 8888
ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
