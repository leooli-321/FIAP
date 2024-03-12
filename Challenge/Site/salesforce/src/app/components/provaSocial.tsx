function ProvaSocial() {
    return (

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
    )
}

export default ProvaSocial;