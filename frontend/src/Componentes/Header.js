import React from 'react';
import FacebookIcon from '@material-ui/icons/Facebook';
import WhatsAppIcon from '@material-ui/icons/WhatsApp';
import TwitterIcon from '@material-ui/icons/Twitter';
import imgLocatel from '../img/locatel.png'
 

export const Header = () =>{

    const link= window.location.href;

    return(<>
        <div className="Header" >
            <div className="Triangulo-left animate__animated animate__fadeInUp"></div>
            <div className="Fondo1" >
                <div className="Triangulo-right animate__animated animate__fadeInUp"></div>
            </div>
            <div className="HeaderContenedorTexto">
                <div className="HeaderLogoContainer">
                    <div className="HeaderLogo" ></div>
                    <div className="HeaderLocatel img-fluid" >
                        <img src={imgLocatel} alt="Logo locatel" className="img-fluid"/>
                    </div>
                </div>
                <div className="HeaderTitulo" ><div className="HeaderOxigeno" >oxígeno<span className="black"> cdmx</span></div></div>
                <div className="HeaderTexto" >Información actualizada todos los días para comprar, rentar o recargar tanques de oxígeno en la Ciudad de México.</div>            
            </div>
            <div className="HeaderBotonesRedes animate__animated animate__fadeIn animate__duration-1s animate__delay-1s" >
                <a href="https://www.facebook.com/sharer/sharer.php?u=oxigenocdmx.cc" target="_blank" rel="noreferrer" aria-label="Share on Facebook" className="HeaderFacebook" >
                    
                        <FacebookIcon className="logofacebook"  />
                        <div>Compartir</div>
                    
                </a>
                
                <a className="HeaderWhatsapp" href="https://api.whatsapp.com/send?text=https://oxigenocdmx.cc" target="_blank" rel="noreferrer" >
                    <WhatsAppIcon className="logowhatsapp" />
                    <div>Compartir</div>
                </a>
                <a className="HeaderTwitter" href="https://twitter.com/intent/tweet?text=https://oxigenocdmx.cc"  target="_blank" rel="noreferrer" aria-label="Share on Twitter">
                    <TwitterIcon className="logotwitter" />
                    <div>Compartir</div>
                </a>
            </div>
        </div></>
    );
}