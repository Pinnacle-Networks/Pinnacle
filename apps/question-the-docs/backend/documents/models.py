import typing as t

from pydantic import BaseModel, Field


class Repo(str):
    pinnacledb = 'pinnacledb'
    langchain = 'langchain'
    fastchat = 'fastchat'


class Query(BaseModel):
    query: str = Field(...)
    collection_name: Repo = Field(...)


class Answer(BaseModel):
    answer: str = Field(...)
    source_urls: list = Field(...)
