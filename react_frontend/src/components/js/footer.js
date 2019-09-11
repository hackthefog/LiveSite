import React from "react"
import footerStyles from "../modules/footer.module.css"
import SocialMedia from "./social-media"

export default () => (
	<div className={footerStyles.footer}>
		<p className={footerStyles.biggerlol}>Follow Us</p>
		<SocialMedia/>
		<p className={footerStyles.tiny}>Fiscally sponsored by The Hack Foundation.</p>
		<p className={footerStyles.tiny}>Nonprofit EIN: 81-2908499.</p>
	</div>
)