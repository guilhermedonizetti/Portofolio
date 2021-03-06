window.$crisp=[];
    window.CRISP_WEBSITE_ID="b9c20f8e-079b-4535-9448-0b8e5dcf4a20";
	(function(){
		d=document;
		s=d.createElement("script");
		s.src="https://client.crisp.chat/l.js";
		s.async=1;
		d.getElementsByTagName("head")[0].appendChild(s);
	})
();

$("#tituloTecnologia").on("click", function(){

    var status = $("#controlTecnologia").val();

    if (status == "fechado") {
        $("#controlTecnologia").val("aberto");
    
        $("#iconTecnologiaRight").css('display', 'none');
        $("#iconTecnologiaDown").css('display', 'inline');

        $("#areaTecnologias").show(500);
    }
    else {
        $("#controlTecnologia").val("fechado");
    
        $("#iconTecnologiaRight").css('display', 'inline');
        $("#iconTecnologiaDown").css('display', 'none');

        $("#areaTecnologias").toggle(500);
    }
});

$("#tituloCurso").on("click", function(){

    var status = $("#controlCurso").val();

    if (status == "fechado") {
        $("#controlCurso").val("aberto");
    
        $("#iconCursoRight").css('display', 'none');
        $("#iconCursoDown").css('display', 'inline');

        $("#areaCurso").show(500);
    }
    else {
        $("#controlCurso").val("fechado");
    
        $("#iconCursoRight").css('display', 'inline');
        $("#iconCursoDown").css('display', 'none');

        $("#areaCurso").toggle(500);
    }
});

$("#tituloFormacao").on("click", function(){

    var status = $("#controlFormacao").val();

    if (status == "fechado") {
        $("#controlFormacao").val("aberto");
    
        $("#iconFormacaoRight").css('display', 'none');
        $("#iconFormacaoDown").css('display', 'inline');

        $("#areaFormacao").show(500);
    }
    else {
        $("#controlFormacao").val("fechado");
    
        $("#iconFormacaoRight").css('display', 'inline');
        $("#iconFormacaoDown").css('display', 'none');

        $("#areaFormacao").toggle(500);
    }
});

$("#tituloExperiencia").on("click", function(){

    var status = $("#controlExperiencia").val();

    if (status == "fechado") {
        $("#controlExperiencia").val("aberto");
    
        $("#iconExperienciaRight").css('display', 'none');
        $("#iconExperienciaDown").css('display', 'inline');

        $("#areaExperiencia").show(500);
    }
    else {
        $("#controlExperiencia").val("fechado");
    
        $("#iconExperienciaRight").css('display', 'inline');
        $("#iconExperienciaDown").css('display', 'none');

        $("#areaExperiencia").toggle(500);
    }
});

$("#tituloIdiomas").on("click", function(){

    var status = $("#controlIdiomas").val();

    if (status == "fechado") {
        $("#controlIdiomas").val("aberto");
    
        $("#iconIdiomasRight").css('display', 'none');
        $("#iconIdiomasDown").css('display', 'inline');

        $("#areaIdiomas").show(500);
    }
    else {
        $("#controlIdiomas").val("fechado");
    
        $("#iconIdiomasRight").css('display', 'inline');
        $("#iconIdiomasDown").css('display', 'none');

        $("#areaIdiomas").toggle(500);
    }
});
