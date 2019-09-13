import React from "react"
import backgroundStyles from "../modules/background.module.css"
import '../../../static/fonts/gotham-rounded/index.css'
import '../../../static/fonts/gotham/index.css'

export default ({children}) => (
	<div className={backgroundStyles.background}>
		<div className={backgroundStyles.overlay}>
			{children}
		</div>
	</div>
)