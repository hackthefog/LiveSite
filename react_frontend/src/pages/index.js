import React from "react"
import Layout from "../components/js/layout"
import SEO from "../components/js/seo"
import Background from "../components/js/background"
import Footer from "../components/js/footer"
import Slideshow from "../components/js/slideshow"
import Team from "../components/js/team"
import Judges from "../components/js/judges"
import Sponsors from "../components/js/sponsors"
import FAQ from "../components/js/faq"
import Schedule from "../components/js/schedule"

const IndexPage = () => (
  <Background>
	  <Layout>
	    <SEO title="Home"/>
	    {/*<h2 style={{fontFamily:`'GothamRounded', Arial`,}}>Welcome to Hack The Fog 2.0!</h2>*/}
	    <Slideshow/>
	    <Schedule/>
	    <FAQ/>
	    <Team/>
	    <Judges/>
	  </Layout>
	  <Sponsors/>
	  <Footer/>
  </Background>
)

export default IndexPage