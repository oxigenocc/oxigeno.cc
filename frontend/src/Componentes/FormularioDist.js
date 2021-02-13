import React from 'react';
import { ContenidoFormulario } from './Formulario/ContenidoFormulario';
import { FooterFormulario } from './Formulario/FooterFormulario';
import {HeaderFormulario} from './Formulario/HeaderFormulario';

export const FormularioDist = () => {
    return (
        <div className="App">
            <HeaderFormulario />
            <ContenidoFormulario />
            <FooterFormulario />
        </div>
    )
}
