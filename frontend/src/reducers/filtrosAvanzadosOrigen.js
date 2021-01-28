import  {types} from "../types/types"; 



export const filtrosAvanzadosOrigen = ( initialState = {
    Estado:false,
    Ciudad:false
}, action )=>{
    switch (action.type) {
        case types.CambiarFiltroOrigen:
            return{
                ...initialState,
                ...action.payload
            };
        
        default:
            return initialState;
    }
}