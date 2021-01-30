import React from 'react';
import Imagen1 from '../img/imagen 1.png';
import Imagen2 from '../img/imagen 2.png';
import ImagenLocatel from '../img/locatel.png';
import logoLight from '../img/logoLight.png';




export const Footer = () =>{

    return(
        <div className="footerContainer">
            <div className="footerLocatel">
                <div>
                    <img src={Imagen1} alt="logo gobierno 1" className="imagen1 img-fluid"></img>   
                    <img src={Imagen2} alt="logo gobierno 2" className="imagen2 img-fluid"></img>           
                </div> 
                <img src={ImagenLocatel} alt="logo locatel" className="imagenLocatelFooter img-fluid"></img>
            </div>
            <div className="footer">
                <div className="copyOxigeno">Oxigeno.cc</div>
                <div className="refLsd">
                    <a href="https://lsdlab.com.mx/" rel="noreferrer" target="_blank">Administrado por Light & Sound Disruptive Lab</a>
                    <div className="contenedorImagen">
                        <a href="https://lsdlab.com.mx/" rel="noreferrer" target="_blank" ><img className="img-fluid imgLogoFooter" alt="logoLightAndSound" src={logoLight} ></img></a>
                    </div>
                </div>
            </div>
        </div>
    );
}