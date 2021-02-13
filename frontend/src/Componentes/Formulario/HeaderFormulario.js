import React from 'react';
import imgLocatel from '../../img/locatel.png'
 

export const HeaderFormulario = () =>{

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
            </div>
        </div></>
    );
}