function Produtos() {
    return (

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
    )
}

export default Produtos;