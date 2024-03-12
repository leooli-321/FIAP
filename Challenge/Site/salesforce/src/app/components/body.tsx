function Body() {
    return (
        <main className="main-content">

            {/*=============== HOME Inicio ===============*/}
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

            {/*=============== About Incorpore recursos ===============*/}
            <section className="about section" id="about">
                <div className="container">
                    {/* section title */}
                    <h2 className="section-title padd-15">About Me</h2>
                    <div className="row">
                        <div className="about-img padd-15">
                            {/* avatar img */}
                            <img src="assets/img/avatar-2.svg" alt="" />
                        </div>
                        <div className="about-content padd-15">
                            <div className="rounded">
                                <div className="row">
                                    <div className="about-text padd-15">
                                        {/* about text */}
                                        <p>I am Bolby Doe, web developer from London, United Kingdom. I have rich experience
                                            in web site design and building and customization, also I am good at WordPress.
                                        </p>
                                        <div>
                                            <a href="#" className="btn btn-default">Download CV</a>
                                        </div>
                                    </div>
                                    <div className="skills padd-15">
                                        <div className="row">
                                            {/* skill item */}
                                            <div className="skill-item">
                                                <h4>Development</h4>
                                                <div className="progress">
                                                    <div className="progress-in"
                                                        style={{ width: "95%", background: "rgb(255,209,92)" }}></div>
                                                    <div className="skill-percent">95%</div>
                                                </div>
                                            </div>
                                            {/* skill item */}
                                            <div className="skill-item">
                                                <h4>Photography</h4>
                                                <div className="progress">
                                                    <div className="progress-in"
                                                        style={{ width: "75%", background: "rgb(255,76,96)" }}></div>
                                                    <div className="skill-percent">75%</div>
                                                </div>
                                            </div>
                                            {/* skill item */}
                                            <div className="skill-item">
                                                <h4>UI/UX design</h4>
                                                <div className="progress">
                                                    <div className="progress-in"
                                                        style={{ width: "85%", background: "rgb(108,108,229)" }}></div>
                                                    <div className="skill-percent">85%</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/*=============== Services Produtos ===============*/}
            <section className="services section">
                <div className="container">
                    {/* section title */}
                    <h2 className="section-title padd-15">Services</h2>
                    <div className="row">
                        {/* service item */}
                        <div className="service-item padd-15">
                            <div className="service-item-inner" style={{ background: "rgb(108,108,229)" }}>
                                <img src="assets/img/service-1.svg" alt="" />
                                <h3>UI/UX design</h3>
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt sapiente dolore.</p>
                            </div>
                        </div>
                        {/* service item */}
                        <div className="service-item padd-15">
                            <div className="service-item-inner" style={{ background: "rgb(249,215,76)" }}>
                                <img src="assets/img/service-2.svg" alt="" />
                                <h3>Web Development</h3>
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt sapiente dolore.</p>
                            </div>
                        </div>
                        {/* service item */}
                        <div className="service-item padd-15">
                            <div className="service-item-inner" style={{ background: "rgb(249,123,139)" }}>
                                <img src="assets/img/service-3.svg" alt="" />
                                <h3>Photography</h3>
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt sapiente dolore.</p>
                            </div>
                        </div>
                    </div>
                    <div className="text padd-15">
                        <p>Looking for a custom job? <a href="#">Click here</a> to contact me! 👋</p>
                    </div>
                </div>
            </section>

            {/*=============== Experience Principais produtos costumer 360 ===============*/}
            <section className="section" id="experience">
                <div className="container">
                    {/* section title */}
                    <h2 className="section-title padd-15">Experience</h2>
                    <div className="row">
                        {/* experience */}
                        <div className="experience padd-15">
                            <div className="row">
                                <div className="timeline-box">
                                    <div className="timeline">
                                        {/* timeline item */}
                                        <div className="timeline-item">
                                            <i className="lni lni-briefcase timeline-icon"></i>
                                            <h3 className="timeline-date">
                                                <i className="lni lni-calendar"></i> 2019 - present
                                            </h3>
                                            <h3 className="timeline-title">Web Designer</h3>
                                            <p className="timeline-text">Lorem ipsum dolor sit amet quo ei simul congue exerci
                                                ad nec admodum perfecto.</p>
                                        </div>
                                        {/* timeline item */}
                                        <div className="timeline-item">
                                            <i className="lni lni-briefcase timeline-icon"></i>
                                            <h3 className="timeline-date">
                                                <i className="lni lni-calendar"></i> 2017 - 2013
                                            </h3>
                                            <h3 className="timeline-title">Front-End Developer</h3>
                                            <p className="timeline-text">Lorem ipsum dolor sit amet quo ei simul congue exerci
                                                ad nec admodum perfecto.</p>
                                        </div>
                                        {/* timeline item */}
                                        <div className="timeline-item">
                                            <i className="lni lni-briefcase timeline-icon"></i>
                                            <h3 className="timeline-date">
                                                <i className="lni lni-calendar"></i> 2013 - 2009
                                            </h3>
                                            <h3 className="timeline-title">Back-End Developer</h3>
                                            <p className="timeline-text">Lorem ipsum dolor sit amet quo ei simul congue exerci
                                                ad nec admodum perfecto.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>


            {/*=============== Pricing Clientes Reais / Prova social ===============*/}
            <section className="section pricing" id="pricing">
                <div className="container">
                    {/* section title */}
                    <h2 className="section-title padd-15">Pricing Plans</h2>
                    <div className="row">
                        {/* prices */}
                        <div className="prices">
                            <div className="price-item">
                                <img src="assets/img/price-1.svg" alt="" />
                                <h3 className="plan">Basic</h3>
                                <p>A Simple option but powerful to manage your business</p>
                                <p>Email support</p>
                                <h3 className="price"><em>$</em>9<span>Month</span></h3>
                                <a href="#" className="btn btn-default">Get Started</a>
                            </div>
                        </div>
                        {/* prices */}
                        <div className="prices">
                            <div className="price-item best">
                                <span className="badge">Recommended</span>
                                <img src="assets/img/price-2.svg" alt="" />
                                <h3 className="plan">Premium</h3>
                                <p>Unlimited product including app integration and more features</p>
                                <p>Email support</p>
                                <h3 className="price"><em>$</em>49<span>Month</span></h3>
                                <a href="#" className="btn btn-default">Get Started</a>
                            </div>
                        </div>
                        {/* prices */}
                        <div className="prices">
                            <div className="price-item">
                                <img src="assets/img/price-3.svg" alt="" />
                                <h3 className="plan">Basic</h3>
                                <p>A wise option for large companies and individuals</p>
                                <p>24/7 support</p>
                                <h3 className="price"><em>$</em>99<span>Month</span></h3>
                                <a href="#" className="btn btn-default">Get Started</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="container">

                    {/* <!-- contact form --> */}
                    <form action="" className="contact-form padd-15">
                        <a href="#" className="btn btn-default">Send Message</a>
                    </form>
                </div>
            </section>


            {/* <!--=============== Footer =============== --> */}
            <footer className="footer">
                <div className="container">
                    <div className="footer-text padd-15">
                        <p>&copy; Cryptical Coder Template</p>
                    </div>
                </div>
            </footer>
        </main >
    );
}

export default Body;