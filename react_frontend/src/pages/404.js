import React from "react"
import Background from "../components/js/background"
import Layout from "../components/js/layout"
import SEO from "../components/js/seo"
import {Link} from "gatsby"
import logo from "../images/inverted_logo.svg"

const NotFoundPage = () => (
	<Background>
		<Layout>
		    <SEO title="404: Not found" />
		    <div style={{
		    	width: `calc(100% - 50px)`,
		    	textAlign: `center`,
		    	margin: `10px auto`,
		    	borderRadius: `10px`,
		    	backgroundColor: `rgba(255,255,255,0.5)`,
		    	height: `80vh`,
		    }}>
			    <h1>ERROR 404 NOT FOUND</h1>
			    <p>Whoops! Seems like this page doesn't exist! Press our logo to go back to our home page!</p>
				<Link><img src={logo} alt="Back Home"></img></Link>
			</div>
		</Layout>
	</Background>
)

export default NotFoundPage