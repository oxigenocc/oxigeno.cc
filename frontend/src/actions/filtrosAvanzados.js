import { types } from "../types/types";


export const filtroTanqueVenta = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            tanqueVenta: value
        }
    }
}


export const filtroTanqueRenta = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            tanqueRenta: value
        }
    }
}


export const filtroTanqueRecarga = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            tanqueRecarga: value
        }
    }
}

export const filtroConcentradorVenta = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            concentradorVenta: value
        }
    }
}


export const filtroConcentradorRenta = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            concentradorRenta: value
        }
    }
}

export const filtroDomicilio = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            domicilioSwitch: value
        }
    }
}

export const filtroTarjeta = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            tarjetaSwitch: value
        }
    }
}

export const filtroAbiertoFin = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            abiertoFin: value
        }
    }
}

export const filtroAbierto24 = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            abierto24: value
        }
    }
}

export const filtroGratis = (value)=>{
    return{
        type: types.CambiarFiltro,
        payload:{
            gratis: value
        }
    }
}