import React from "react"
import imageButtonStyles from "../modules/image-link-container.module.css"

export default (props) => (
	<a className={imageButtonStyles.imageButton} href={props.linkto}>
		{props.children}
	</a>
)