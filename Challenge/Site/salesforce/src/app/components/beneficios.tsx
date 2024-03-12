function Beneficios() {
    return (

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
    )
}


export default Beneficios;