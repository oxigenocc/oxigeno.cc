import { createStore, combineReducers } from 'redux';
import { filtrosAvanzadosOrigen } from '../reducers/filtrosAvanzadosOrigen';
import {filtrosAvanzadosReducer} from "../reducers/filtrosAvanzadosReducer";

const reducers = combineReducers({
    filtrosAvanzadosCiudad: filtrosAvanzadosOrigen,
    filtrosAvanzados: filtrosAvanzadosReducer
})

export const store = createStore(
    reducers,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);