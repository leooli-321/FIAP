import './style.css'

const Header = () => {
    return (
        <header className="header">
            <h1>Título</h1>
            <nav>
                <ul>
                    <li>
                        <a href="#">Home</a>
                        <a href="#">Contatos</a>
                        <a href="#">Quem Somos</a>
                        <a href="#">Perfil</a>
                    </li>
                </ul>
            </nav>
        </header>
    )
}

export default Header