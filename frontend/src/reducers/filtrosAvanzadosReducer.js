import  {types} from "../types/types"; 



export const filtrosAvanzadosReducer = ( initialState = {
    tanqueVenta: false,
    tanqueRenta: false,
    tanqueRecarga: false,
    concentradorVenta: false,
    concentradorRenta:false,
    domicilioSwitch:false,
    tarjetaSwitch:false,
    abiertoFin: false,
    abierto24: false,
    gratis: false
}, action )=>{
    switch (action.type) {
        case types.CambiarFiltro:
            return{
                ...initialState,
                ...action.payload
            };
        
        default:
            return initialState;
    }
}