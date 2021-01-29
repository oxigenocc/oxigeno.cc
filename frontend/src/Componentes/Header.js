import React from 'react';
import FacebookIcon from '@material-ui/icons/Facebook';
import WhatsAppIcon from '@material-ui/icons/WhatsApp';
import TwitterIcon from '@material-ui/icons/Twitter';
import imgLocatel from '../img/locatel.png'
 

export const Header = () =>{

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
                <div className="HeaderTitulo" ><div className="HeaderOxigeno" >oxígeno <span className="black">cc</span></div></div>
                <div className="HeaderTexto" >Información actualizada todos los días para comprar, rentar o recargar tanques de oxígeno en la Ciudad de México.</div>            
            </div>
            <div className="HeaderBotonesRedes animate__animated animate__fadeIn animate__duration-1s animate__delay-1s" >
                <a href="https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Foxigeno.cc%2F" target="_blank" rel="noreferrer" aria-label="Share on Facebook" className="HeaderFacebook" >
                    
                        <FacebookIcon className="logofacebook"  />
                        <div>Compartir</div>
                    
                </a>
                
                <a className="HeaderWhatsapp" href="https://api.whatsapp.com/send?text=https://oxigeno.cc" target="_blank" rel="noreferrer" >
                    <WhatsAppIcon className="logowhatsapp" />
                    <div>Compartir</div>
                </a>
                <a className="HeaderTwitter" href="https://twitter.com/intent/tweet/?text=Informaci%C3%B3n%20actualizada%20todos%20los%20d%C3%ADas%20para%20comprar%2C%20rentar%20o%20recargar%20tanques%20de%20ox%C3%ADgeno%20en%20la%20Ciudad%20de%20M%C3%A9xico.&amp;url=https%3A%2F%2Foxigeno.cc%2F" target="_blank" rel="noreferrer" aria-label="Share on Twitter">
                    <TwitterIcon className="logotwitter" />
                    <div>Compartir</div>
                </a>
            </div>
        </div></>
    );
}