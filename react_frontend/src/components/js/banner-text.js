import React from "react"
import bannerTextStyles from "../modules/banner-text.module.css"

export default ({children}) => (
	<div className={bannerTextStyles.banner}>
		<p className={bannerTextStyles.text}>{children}</p>
	</div>
)