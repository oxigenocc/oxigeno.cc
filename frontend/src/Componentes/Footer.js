import React from 'react';
import Imagen1 from '../img/imagen 1.png';
import Imagen2 from '../img/imagen 2.png';
import ImagenLocatel from '../img/locatel.png';
import logoLight from '../img/logoLight.png';




export const Footer = () =>{

    return(
        <div className="footerContainer">
            <div className="footerPostman">
                <p className="textoPostman">¿Eres programador? puedes usar nuestra API de forma gratuita</p>
                <a href="https://app.getpostman.com/run-collection/90220cc63e76e5062bfd" target="_blank"><div className="botonPostman">Pruébala en postman</div></a>
            </div>
            <div className="footerLocatel">
                <div>
                    <img src={Imagen1} alt="logo gobierno 1" className="imagen1 img-fluid"></img>   
                    <img src={Imagen2} alt="logo gobierno 2" className="imagen2 img-fluid"></img>           
                </div> 
                <img src={ImagenLocatel} alt="logo locatel" className="imagenLocatelFooter img-fluid"></img>
            </div>
            <div className="footer">
                <div className="copyOxigeno">Oxigenocdmx.cc</div>
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