

// export const endPoints = "https://dev-oxigeno.cdmx.gob.mx/api/v2/";

function RemoveLastDirectoryPartOf(the_url)
{
    var the_arr = the_url.split('/');
    the_arr.pop();
    return( the_arr.join('/') );
}

export const endPoints =  `${RemoveLastDirectoryPartOf(window.location.href)}api/v2/`;