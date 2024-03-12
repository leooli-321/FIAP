function Header() {
    return (
        <header className="header" id="header">
            {/* nav */}
            <nav className="nav container padd-15">
                {/* nav logo */}
                <a href="#" className="nav-logo">
                    <h2>SalesForce</h2>
                </a>
                {/* nav menu */}
                <div className="nav-menu" id="nav-menu">
                    {/* nav list */}
                    <ul className="nav-list">
                        <li className="nav-item">
                            <a href="#home" className="nav-link active-link">Início</a>
                        </li>
                        <li className="nav-item">
                            <a href="#about" className="nav-link">Produtos</a>
                        </li>
                        <li className="nav-item">
                            <a href="#experience" className="nav-link">Saiba Mais</a>
                        </li>
                        <li className="nav-item">
                            <a href="#pricing" className="nav-link">Contatos</a>
                        </li>
                        <li className="nav-item">
                            <a href="#portfolio" className="nav-link">LOGIN</a>
                        </li>
                        <li className="nav-item">
                            <a href="#contact" className="nav-link">Teste Grátis</a>
                        </li>
                    </ul>
                    {/* nav close */}
                    <div className="nav-close" id="nav-close">
                        <i className="lni lni-close"></i>
                    </div>
                </div>
                {/* nav btn */}
                <div className="nav-btns">
                    {/* theme change btn */}
                    <i className="lni lni-pallet change-theme" id="theme-button"></i>
                    {/* toggle btn */}
                    <div className="nav-toggle" id="nav-toggle">
                        <i className="lni lni-grid-alt"></i>
                    </div>
                </div>
            </nav>
        </header>
    );
}
export default Header;
