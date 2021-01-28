import  {types} from "../types/types"; 



export const filtrosAvanzadosReducer = ( initialState = {
    tanqueVenta: false,
    tanqueRenta: false,
    tanqueRecarga: false,
    concentradorVenta: false,
    concentradorRenta:false,
    domicilioSwitch:false,
    tarjetaSwitch:false
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