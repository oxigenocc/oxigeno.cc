import React,{ useState } from 'react';
import {useForm} from '../../hooks/useForm';
import Checkbox from '@material-ui/core/Checkbox';
import axios from 'axios';
import swal from 'sweetalert';
import {endPoints} from '../../types/endPoints';


export const ContenidoFormulario = () => {

    const [buttonActivado, setButtonActivado] = useState(false)

    const [ boolValues, setBoolValues ] = useState({
        aDomicilio:false,
        pagoConTarjeta: false,
        ofreceVentaDeTanque:false,
        ofreceRentaDeTanque:false,
        ofreceRecargaDeTanque:false,
        ofreceVentaDeConcentrador:false,
        ofreceRentaDeConcentrador:false,
    })

    const initialForm = {
        nombreDistribuidor: '',
        rfc: '',
        telefono: '',
        direccion: '',
        horario: '',
        linkPagina:'',
        whatsapp:'',
    }
    const [ formValues, handleInputChange, reset ] = useForm( initialForm );

    const submit = async(e)=>{
        e.preventDefault();
        setButtonActivado(true);

        if (formValues.nombreDistribuidor ==="" || formValues.rfc==="" || formValues.telefono===""|| formValues.direccion==="" || formValues.horario==="") {
            console.log("Error")
            setButtonActivado(false);
            swal("¡Alerta!", "Por favor llene los campos Requeridos", "warning");
        }else{
            try {
                const peticion= await axios.post(`${endPoints}/formulario/data`,{
                    params:{
                        nombreDistribuidor: formValues.nombreDistribuidor,
                        rfc: formValues.rfc,
                        telefono: formValues.telefono,
                        direccion: formValues.direccion,
                        horario: formValues.horario,
                        linkPagina: formValues.linkPagina,
                        whatsapp: formValues.whatsapp,
                        aDomicilio: boolValues.aDomicilio,
                        pagoConTarjeta: boolValues.pagoConTarjeta,
                        ofreceVentaDeTanque: boolValues.ofreceVentaDeTanque,
                        ofreceRentaDeTanque: boolValues.ofreceRentaDeTanque,
                        ofreceRecargaDeTanque: boolValues.ofreceRecargaDeTanque,
                        ofreceVentaDeConcentrador: boolValues.ofreceVentaDeConcentrador,
                        ofreceRentaDeConcentrador: boolValues.ofreceRentaDeConcentrador,
                    }
                });

                if (await peticion.status ===200) {
                    swal("Solicitud exitosa", "Nos contactaremos contigo lo más pronto posible", "success");
                    setButtonActivado(false);
                }else{
                    swal("¡Ups!", "Lo sentimos, hubo un error al hacer el registro. Por favor intente más tarde", "error");
                    setButtonActivado(false); 
                }

            } catch (error) {
                console.log(error)
                swal("¡Ups!", "Lo sentimos, hubo un error al hacer el registro. Por favor intente más tarde", "error");
                setButtonActivado(false);
            }
        }
    }

    return (
        <div className="formularioContainer">
            <div className="formularioTitulo">Formulario de registro para distribuidores</div>
            <div className="formulariocontenido">
                <div className="formularioFormulario col-12 col-md-10 col-xl-8">
                    <form>
                        <div className="form-group formularioNombre">
                            <label className="formulario-subtitulo" htmlFor="nombreDistribuidor">Nombre de la empresa<span className="red">*</span></label>
                            <input type="text" className="form-control" placeholder="Nombre" name="nombreDistribuidor" onChange={handleInputChange} />
                        </div>

                        <div className="form-group formularioRFCTel">
                            <div className="formularioRFC">
                                <label className="formulario-subtitulo" htmlFor="rfc">RFC<span className="red">*</span></label>
                                <input type="text" className="form-control" placeholder="RFC" name="rfc" onChange={handleInputChange} />
                            </div>
                            <div className="formularioTel">
                                <label className="formulario-subtitulo" htmlFor="telefono">Telefono<span className="red">*</span></label>
                                <input type="text" className="form-control" placeholder="Telefono" name="telefono" onChange={handleInputChange} />
                            </div>
                        </div>

                        <div className="form-group formularioDireccion">
                            <label className="formulario-subtitulo" htmlFor="direccion">Dirección<span className="red">*</span></label>
                            <input type="text" className="form-control" placeholder="Dirección" name="direccion" onChange={handleInputChange} />
                        </div>

                        <div className="form-group formularioHorario">
                            <label className="formulario-subtitulo" htmlFor="horario">Horario<span className="red">*</span></label>
                            <input type="text" className="form-control" placeholder="Horario" name="horario" onChange={handleInputChange} />
                        </div>

                        <div className="form-group formularioWebWhats">
                            <div className="formularioWeb">
                                <label className="formulario-subtitulo" htmlFor="linkPagina">Página web <span className="opcional">(opcional)</span></label>
                                <input type="text" className="form-control" placeholder="Página web" name="linkPagina" onChange={handleInputChange} />
                            </div>
                            <div className="formularioWhats">
                                <label className="formulario-subtitulo" htmlFor="whatsapp">Whatsapp <span className="opcional">(opcional)</span></label>
                                <input type="text" className="form-control" placeholder="Whatsapp" name="whatsapp" onChange={handleInputChange} />
                            </div>
                        </div>

                        <div className="form-group formularioDomicilioTarjeta">
                         
                            <div className="form-check formularioDomicilio" >
                                <div className="formulario-subtitulo"><label htmlFor="aDomicilio">Servicio a domicilio</label></div>
                                <div className="domicilioBoton">
                                    <span>¿Ofreces servicio a domicilio?</span>
                                    <Checkbox
                                        checked={boolValues.aDomicilio}
                                        onChange={() => setBoolValues({ ...boolValues, aDomicilio: !boolValues.aDomicilio})}
                                        name="aDomicion"
                                        color="primary"
                                    />

                                </div>
                            </div>

                            <div className="form-check formularioTarjeta" >
                                <div className="formulario-subtitulo"><label htmlFor="pagoConTarjeta">Pago con tarjeta</label></div>
                                <div className="tarjetaBoton">
                                    <span>¿Ofreces pago con tarjeta?</span>
                                    <Checkbox
                                        checked={boolValues.pagoConTarjeta}
                                        onChange={() => setBoolValues({ ...boolValues, pagoConTarjeta: !boolValues.pagoConTarjeta})}
                                        name="pagoConTarjeta"
                                        color="primary"
                                    />
                                </div>
                            </div>
                        </div>

                        <div className="form-group formularioTanquesConcentradores">
                         
                            <div className="form-check formularioTanques" >
                                <div className="formulario-subtitulo"><label htmlFor="ofreceVentaDeTanque">Tanques</label></div>
                                <div className="botonTanques">
                                    <span>Venta de tanques</span>
                                    <Checkbox
                                        checked={boolValues.ofreceVentaDeTanque }
                                        onChange={() => setBoolValues({ ...boolValues, ofreceVentaDeTanque  : !boolValues.ofreceVentaDeTanque })}
                                        name="ofreceVentaDeTanque"
                                        color="primary"
                                    />
                                </div>
                                <div className="botonTanques">
                                    <span>Renta de tanques</span>
                                    <Checkbox
                                        checked={boolValues.ofreceRentaDeTanque }
                                        onChange={() => setBoolValues({ ...boolValues, ofreceRentaDeTanque  : !boolValues.ofreceRentaDeTanque })}
                                        name="ofreceRentaDeTanque"
                                        color="primary"
                                    />
                                </div>
                                <div className="botonTanques">
                                    <span>Recarga de tanques</span>
                                    <Checkbox
                                        checked={boolValues.ofreceRecargaDeTanque }
                                        onChange={() => setBoolValues({ ...boolValues, ofreceRecargaDeTanque  : !boolValues.ofreceRecargaDeTanque })}
                                        name="ofreceRecargaDeTanque"
                                        color="primary"
                                    />                                
                                </div>
                            </div>

                            <div className="form-check formularioConcentradores" >
                                <label className="formulario-subtitulo" htmlFor="ofreceVentaDeConcentradores">Concentradores</label>
                                <div className="botonConcentradores">
                                    <span>Venta de concentradores</span>
                                    <Checkbox
                                        checked={boolValues.ofreceVentaDeConcentrador }
                                        onChange={() => setBoolValues({ ...boolValues, ofreceVentaDeConcentrador  : !boolValues.ofreceVentaDeConcentrador })}
                                        name="ofreceVentaDeConcentrador"
                                        color="primary"
                                    />                                </div>
                                <div className="botonConcentradores">
                                    <span>Renta de concentradores</span>
                                    <Checkbox
                                        checked={boolValues.ofreceRentaDeConcentrador }
                                        onChange={() => setBoolValues({ ...boolValues, ofreceRentaDeConcentrador  : !boolValues.ofreceRentaDeConcentrador })}
                                        name="ofreceRentaDeConcentrador"
                                        color="primary"
                                    />                                </div>
                            </div>
                        </div>

                        <div className="botonSubmit"><button disabled={buttonActivado} type="submit" className="btn btn-primary" onClick={(e)=>submit(e)}>Confirmar</button></div>
                    </form> 
                </div>
            </div>
        </div>
    )
}
