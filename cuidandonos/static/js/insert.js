var campos_max = 100;   //max de campos
var x = 0;
$('#add_field').click(function (e) {
        e.preventDefault();     //prevenir nuevos clicks
        if (x < campos_max) {
                $('#divBeneficiarios').append(
                        '<div>\
                        <div class="form-group row">\
                                        <label for="inputNombreBenef[]" class="col-sm-6 col-form-label">Nombre y Apellido</label>\
                                        <label for="inputDniBenef[]" class="col-sm-6 col-form-label">DNI</label>\
                                        <div class="col-sm-6">\
                                                <input type="text" name="inputNombreBenef[]" class="form-control" id="inputNombreBenef[]"\
                                        placeholder="Nombre y Apellido">\
                                        </div>\
                                        <div class="col-sm-6">\
                                                <input type="number" name="inputDniBenef[]" class="form-control" id="inputDniBenef[]"\
                                                placeholder="DNI">\
                                        </div>\
                                </div>\
                        <a href="#" class="remover_campo">Remover</a>\
                        </div >\
                        ');
                x++;
        }
});
// Remover div anterior
$('#divBeneficiarios').on("click", ".remover_campo", function (e) {
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
});

var colab_max = 100;   //max de colab
var y = 0;
$('#add_colab').click(function (e) {
        e.preventDefault();     //prevenir nuevos clicks
        if (y < colab_max) {
                $('#divColaboradores').append(
                        '<div>\
                        <div class="form-group row">\
                            <label for="inNomColab[]" class="col-sm-1 col-form-label">Nombre</label>\
                            <div class="col-sm-4">\
                            <input type="text" class="form-control" id="inNomColab[]" placeholder="Nombre">\
                            </div>\
                            <label for="inApColab[]" class="col-sm-1 col-form-label">Apellido</label>\
                            <div class="col-sm-4">\
                            <input type="text" class="form-control" id="inApColab[]" placeholder="Apellido">\
                            </div>\
                        </div>\
                        <div class="form-group row">\
                            <label for="inDniColab[]" class="col-sm-1 col-form-label">Dni</label>\
                            <div class="col-sm-4">\
                            <input type="number" class="form-control" id="inDniColab[]" placeholder="Dni">\
                            </div>\
                            <label for="inCuilColab" class="col-sm-1 col-form-label">Cuil</label>\
                            <div class="col-sm-4">\
                            <input type="number" class="form-control" id="inCuilColab[]" placeholder="00-00000000-00">\
                            </div>\
                        </div>\
                    <a href="#" class="remover_campo">Remover</a>\
                </div>\
              ');
                y++;
        }
});
// Remover div anterior
$('#divColaboradores').on("click", ".remover_campo", function (e) {
        e.preventDefault();
        $(this).parent('div').remove();
        y--;
});

// mostrar/ocultar 
$(document).ready(function () {
        $(".rdPersJur").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#PersJur1").css("display", "block");
                        $("#PersJur2").css("display", "block");
                } else {
                        $("#PersJur1").css("display", "none");
                        $("#PersJur2").css("display", "none");
                }
        });

        $(".rdBenefMinDes").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#BenefMinDes").css("display", "block");
                        // $("#PersJur2").css("display", "block");
                } else {
                        $("#BenefMinDes").css("display", "none");
                        // $("#PersJur2").css("display", "none");
                }
        });

        $(".rdRemMinDes").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#RemMinDes").css("display", "block");
                        // $("#PersJur2").css("display", "block");
                } else {
                        $("#RemMinDes").css("display", "none");
                        // $("#PersJur2").css("display", "none");
                }
        });

        $(".rdAguaPot").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#tipoConex0").css("display", "block");
                        $("#tipoConex1").css("display", "block");
                        $("#tipoConex2").css("display", "block");
                } else {
                        $("#tipoConex0").css("display", "none");
                        $("#tipoConex1").css("display", "none");
                        $("#tipoConex2").css("display", "none");
                }
        });

        $(".rdInstSanitarias").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dChkSanitarios1").css("display", "block");
                        $("#dChkSanitarios2").css("display", "block");
                        $("#dChkSanitarios3").css("display", "block");
                } else {
                        $("#dChkSanitarios1").css("display", "none");
                        $("#dChkSanitarios2").css("display", "none");
                        $("#dChkSanitarios3").css("display", "none");
                }
        });

        $(".rdGeriatria").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvSubirDoc").css("display", "block");

                } else {
                        $("#dvSubirDoc").css("display", "none");

                }
        });

        $(".rdExperiencia").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvLugarExp").css("display", "block");

                } else {
                        $("#dvLugarExp").css("display", "none");

                }
        });

        $(".rdLugarExperiencia").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'Institucion') {
                        $("#dvInstitucion").css("display", "block");
                        $("#dvDomicilio").css("display", "none");
                        $("#dvClinica").css("display", "none");
                        $("#dvFamiliar").css("display", "none");
                } else if (valor == 'Domicilio') {
                        $("#dvInstitucion").css("display", "none");
                        $("#dvDomicilio").css("display", "block");
                        $("#dvClinica").css("display", "none");
                        $("#dvFamiliar").css("display", "none");

                } else if (valor == 'Clinica') {
                        $("#dvInstitucion").css("display", "none");
                        $("#dvDomicilio").css("display", "none");
                        $("#dvClinica").css("display", "block");
                        $("#dvFamiliar").css("display", "none");
                } else {
                        $("#dvInstitucion").css("display", "none");
                        $("#dvDomicilio").css("display", "none");
                        $("#dvClinica").css("display", "none");
                        $("#dvFamiliar").css("display", "block");
                }
        });

        $(".rdCoopTr").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvCoopTr").css("display", "block");

                } else {
                        $("#dvCoopTr").css("display", "none");

                }
        });

        $(".rdEstudiante").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvEstudios").css("display", "block");

                } else {
                        $("#dvEstudios").css("display", "none");

                }
        });

        $(".rdOrg").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvOrg").css("display", "block");

                } else {
                        $("#dvOrg").css("display", "none");

                }
        });

        $(".rdTrabaja").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvTrabaja").css("display", "block");

                } else {
                        $("#dvTrabaja").css("display", "none");

                }
        });

        $(".rdProfesion").click(function (evento) {

                var valor = $(this).val();

                if (valor == 'si') {
                        $("#dvProfesion").css("display", "block");

                } else {
                        $("#dvProfesion").css("display", "none");

                }
        });

        // COMEDORES LOCALIDADES / PROVINCIAS

        $.getJSON('../static/js/provincias.json', function (data) {
                $.each(data.provincias, function (i, provincias) {
                        $("#selProvincias").append('<option value=" ' + provincias.id + '" name="' + provincias.id + '">' + provincias.iso_nombre + '</option>');
                }); // close each()
        }); // close getJSON()


        // $(function () {

        var fillselLocalidades = function () {

                var selected = $('#selProvincias').val();
                if (!selected) { selected = 22; }
                $('#selLocalidades').empty();
                $.getJSON('../static/js/municipios.json', function (data) {
                        //console.log(selected);


                        $.each(data.municipios, function (i, municipios) {
                                var provId = parseInt(data.municipios[i].provincia.id);
                                // console.log(selected);
                                // console.log(data.municipios[i].provincia.id);
                                if (provId == selected) {

                                        // console.log(data.municipios[i].provincia.id);
                                        $('#selLocalidades').append('<option value="' + municipios.id + '">' + municipios.nombre + '</option>');
                                }
                        });
                });
        }
        $('#selProvincias').change(fillselLocalidades);
        fillselLocalidades();


        // });




});