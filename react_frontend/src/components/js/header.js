import { Link } from "gatsby"
import PropTypes from "prop-types"
import React from "react"
import logo from "../../images/inverted_logo.svg"

const Header = ({ siteTitle }) => (
  <header
    style={{
      background: `rgba(32, 122, 238, 0.6)`,
      margin: `0rem`,
      paddingLeft: `0.5rem`,
    }}
  >
    <div
      style={{
        margin: `0 auto`,
        width: `100%`,
        padding: `10px`,
      }}
    >
    <Link to="/">
      <img src={logo} alt="Hack The Fog 2.0" styles={{width: `77px`, height: `50px`,}}></img>
    </Link>
    </div>
  </header>
)

export default Header
