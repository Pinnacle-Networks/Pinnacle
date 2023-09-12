import pinnacledbLogo from '../assets/pinnacledb.svg'

const Header = () => {

    return (
        <div className='banner'>
            <a href="https://pinnacledb.com" target="_blank">
                <img src={pinnacledbLogo} className="logo" alt="SuperDuperDB logo" />
            </a>
            <h1 className='title'>Question the Docs</h1>
        </div>
    )
};

export default Header;