function Inicio() {
    return (
        <section className="home" id="home">
            <div className="container">
                {/* intro */}
                <div className="intro">
                    {/* avatar image */}
                    <img src="src/app/img/avatar-1.svg" alt="Bolby" />
                    {/* info */}
                    <br />
                    <span> <span className="info-text">Bem vindo a</span></span>

                    <h1>Salesforce</h1>
                    {/* social icons */}
                    <ul className="social-icons">
                        <li><a href="#"><i className="lni lni-instagram-original"></i></a></li>
                        <li><a href="#"><i className="lni lni-twitter-original"></i></a></li>
                        <li><a href="#"><i className="lni lni-behance-original"></i></a></li>
                        <li><a href="#"><i className="lni lni-dribbble"></i></a></li>
                        <li><a href="#"><i className="lni lni-pinterest"></i></a></li>
                    </ul>
                    {/* button */}
                    <div>
                        <a href="#" className="btn btn-default">Hire me</a>
                    </div>
                    {/* scroll down mouse wheel */}
                    <div className="scroll-down">
                        <a href="#" className="mouse-wrapper">
                            <span>Scroll Down</span>
                            <span className="mouse">
                                <span className="wheel"></span>
                            </span>
                        </a>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Inicio;