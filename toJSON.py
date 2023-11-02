import re
import json
import json

# The text from the file
text = """
Documento: 8
Articulo: 3
Capitulo: I - CONVOCATORIA

Norma General: Las convocatorias para la designacion por Concurso de Profesores Ordinarios titulares, asociados y adjuntos para las diferentes catedras, areas, nucleos, asignaturas que integran los nucleos, disciplinas, laboratorio de las Facultades que integran esta Universidad se regiran por las disposiciones del presente Reglamento y las que en consecuencia dicten las Unidades Academicas, que deberan ser aprobadas por el Consejo Superior.


Documento: 8
Articulo: 4
Capitulo: I - CONVOCATORIA

Cada Unidad Academica mediante Resolucion del Consejo Directivo propondra al Consejo Superior la provision de cargos de profesores por concurso especificando lo siguiente: a) las catedras, areas, nucleos, asignaturas que integran los nucleos, disciplinas, laboratorio a concursar. b) La categoria. c) La dedicacion. d) Si la imputacion presupuestaria correspondiente al cargo llamado esta afectada a la partida Gastos de Personal En todos los casos, el Consejo Superior debera resolver sobre la solicitud de llamado dentro de los treinta (30) dias de recibida.


Documento: 8
Articulo: 5
Capitulo: I - CONVOCATORIA

Las Unidades Academicas mediante resolucion de sus Consejos Directivos podran proponer al Consejo Superior la realizacion de concursos conjuntamente con otras Unidades Academicas de esta Universidad.


Documento: 8
Articulo: 6
Capitulo: II - PUBLICIDAD

Difusion: La difusion del llamado a concurso estara a cargo del Rectorado quien publicara dentro de los diez (10) dias de aprobado el llamado a concurso, haciendo como minimo un aviso por un (1) dia en un diario de circulacion nacional y debiendose publicar por tres (3) dias, en un diario de la localidad sede y subsede de la Unidad Academica respectiva. En aquellas localidades en las que la tirada de los diarios sea de frecuencia semanal bastara con una sola publicacion. En todos los casos, la publicidad debera efectuarse entre los diarios de mayor tirada. El rectorado se hara cargo ademas, de la difusion del llamado a traves de los medios de comunicacion con que contara y las Unidades Academicas comunicaran asimismo a sus similares afines dentro del ambito universitario nacional y a los medios de difusion que consideren convenientes. Las respectivas publicaciones se deberan agregar para constancia al expediente de Concurso.


Documento: 8
Articulo: 8
Capitulo: II - PUBLICIDAD

Contenido: Los anuncios contendran sinteticamente: - Los cargos y en su caso funcion a concursar; la categoria y la dedicacion de los mismos, explicitando que el concursante puede ofrecer una dedicacion distinta a la indicada. - La fecha de apertura de la inscripcion y la fecha y hora de cierre de la misma. - El lugar y dependencia habilitada de la Unidad Academica donde se recibiran las inscripciones y se proporcionara toda la informacion necesaria.


Documento: 8
Articulo: 9
Capitulo: III - INSCRIPCION

Condiciones de los aspirantes: Para presentarse a Concurso el aspirante debe reunir los siguientes requisitos: a) Tener titulo universitario de grado o en su defecto acreditar antecedentes excepcionales que lo suplan, y b) no estar comprendido en las causales de inhabilitacion para el desempeno de cargos publicos y de faltas a la etica universitaria que se mencionan en el articulo 18 del presente Reglamento.


Documento: 8
Articulo: 10
Capitulo: III - INSCRIPCION

Plazo de Inscripcion: En las Unidades Academicas correspondientes alllamado, se abrira un periodo de inscripcion por el termino de veinte (20) dias, considerandose como fecha de iniciacion de ese periodo el dia que el Decano establezca en resolucion dictada especialmente al efecto dentro de los tres (3) dias de aprobado el llamado.


Documento: 8
Articulo: 11
Capitulo: III - INSCRIPCION

Oficina de Inscripcion: Las inscripciones se realizaran en la Mesa de Entradas de cada Facultad. Al mismo tiempo, las Unidades Academicas habilitaran una dependencia donde los aspirantes seran asesorados en todo cuanto se refiere a su presentacion.


Documento: 8
Articulo: 12
Capitulo: III - INSCRIPCION

Solicitud de Inscripcion: Las solicitudes de inscripcion tendran el caracter de Declaracion Jurada y seran presentadas, bajo recibo en el que constara la fecha y hora derecepcion, por los aspirantes o personas autorizadas, en la dependencia habilitada en larespectiva Unidad Academica en un (1) original y cinco (5) copias y, ademas, en soporte digital, con la informacion basica siguiente: 1) Apellido y nombres, nacionalidad, estado civil, fecha y lugar de nacimiento, clase y numero de documento de identidad, domicilio real y constituir el especial dentro de la ciudad asiento de la Unidad Academica o en un radio de hasta 30 km de la misma. 2) Titulo universitario, con indicacion de la Facultad y Universidad que lo otorgo. Los titulos universitarios deberan presentarse en original y fotocopia simple la que sera autenticada por personal autorizado por la Facultad. En su defecto podran presentarse fotocopias legalizadas ante escribano publico o juez de paz. 3) Titulos no universitarios, si los tuviere, con indicacion de la Entidad que los otorgo, los que deberan presentarse bajo las mismas formalidades indicadas en el inciso anterior. RESOLUCION No289/08. 4) La totalidad de los antecedentes docentes y no docentes e indole de las tareas desarrolladas, indicando la institucion, el periodo de ejercicio y la naturaleza de su designacion. 5) Nomina de obras y publicaciones, consignando la editorial o revista y lugar y fecha depublicacion. Los miembros del jurado podran exigir que se presenten copias u originales de las publicaciones y trabajos realizados, las que seran devueltas una vez sustanciado el Concurso. 6) Otros antecedentes relacionados con la especialidad, tales como cursos realizados, conferencias dictadas, etc. 7) La totalidad de los antecedentes que hagan a su actuacion en Universidades e Instituciones nacionales, provinciales y privadas, registradas en el pais o en el extranjero; cargo que desempeno o desempena en la Administracion Publica o en la actividad privada, en el pais o en el extranjero. Los antecedentes de Instituciones extranjeras deberan presentarse acompanados de su traduccion al espanol. 8) Participacion en Congresos o acontecimientos similares, nacionales o internacionales. 9) Distinciones, premios y becas obtenidas. 10) Una sintesis de los aportes originales efectuados en el ejercicio de la especialidad respectiva. 11) Una sintesis de la actuacion profesional. 12) Otros cargos y antecedentes que a juicio del aspirante pueden contribuir a una mejorilustracion sobre su competencia en la materia en Concurso. Indicacion de la dedicacion o dedicaciones a que aspira, o bien que el aspirante proponga una distinta a la consignada en el respectivo llamado.


Documento: 8
Articulo: 13
Capitulo: III - INSCRIPCION

Documentacion Probatoria: Los aspirantes deberan adjuntar la documentacion que acredite fehacientemente todos los titulos y antecedentes invocados en su presentacion, en original o en copia autenticada en la Oficina de Inscripcion, en las Unidades Academicas, a traves de sus sedes y subsedes o por funcionario publico. Esta documentacion podra ser retirada de la oficina una vez concluido el tramite de Concurso o cuando ocurra desistimiento del aspirante. La documentacion probatoria, podra ser completada por los aspirantes hasta seis (6) dias despues de vencido el plazo para la inscripcion, cuando por cualquier motivo no pudieran adjuntarla a la presentacion, pero en ningun caso se aceptara documentacion recibida fuera de este termino suplementario.


Documento: 8
Articulo: 14
Capitulo: III - INSCRIPCION

Planeamiento de Catedra: Juntamente con la solicitud de inscripcion, los aspirantes deberan presentar - de acuerdo a la modalidad de la convocatoria realizada - un trabajo de Planeamiento de Catedra en el que se expidan sobre la insercion de la asignaturaen el Plan de Estudio, Programa de la asignatura, criterios pedagogicos, bibliografia, organizacion de la Catedra y cuando sea aplicable, investigacion y extension. RESOLUCION No289/08. El trabajo referido debera presentarse en un (1) original y cinco (5) copias en sobres cerrados para su envio a los miembros del Jurado y archivo.


Documento: 8
Articulo: 15
Capitulo: III - INSCRIPCION

Presentacion irregular y tardia: El responsable de Mesa de Entradas, dispondra sin mas tramites la devolucion de las presentaciones que no se ajusten a los requisitos formales establecidos en este Reglamento o que se reciban fuera de termino.


Documento: 8
Articulo: 16
Capitulo: III - INSCRIPCION

Si transcurridos tres (3) meses a contar del cierre de la inscripcion, el jurado no se hubiere constituido, el aspirante tendra derecho a ampliar sus antecedentes hasta que aquel se constituya.


Documento: 8
Articulo: 17
Capitulo: III - INSCRIPCION

Apoderado: Los aspirantes podran inscribirse e intervenir en los restantes tramites por intermedio de apoderados expresamente facultados para ello, mediante poder otorgado por escribano publico debidamente legalizado o de acuerdo a la ley 7060. El apoderado no podra ser otro inscripto en la misma disciplina que concurse el poderdante, ni un miembro del Jurado. Tampoco podran ejercer la representacion el Rector, los Secretarios Politicos del Rectorado, los Decanos o Delegados del Rector, los Secretarios Academicos de las Facultades y Escuelas, los miembros del Consejo Superior y del Consejo Directivo de la respectiva Unidad Academica donde tramite el Concurso, y el personal administrativo de la Universidad Autonoma de Entre Rios. Si la incompatibilidad surgiera en cualquier etapa del tramite, el apoderado debera ser reemplazado dentro de los cinco (5) dias en que aquella se produjera, lapso durante el cual quedaran suspendidos los terminos.


Documento: 8
Articulo: 18
Capitulo: III - INSCRIPCION

Inscripciones multiples: El aspirante que se presente a mas de un Concurso debera cumplir en cada uno de ellos con todos los requisitos establecidos en esta ordenanza, sin poder remitirse a los escritos o documentos presentados en los otros. Si los Concursos a los que se presenta integran el mismo llamado de una Unidad Academica, basta que el aspirante cumplimente en uno de ellos la exigencia del articulo 10, refiriendose en las solicitudes de inscripcion de los otros Concursos, en cual agrego la documentacion que menciona el citado articulo y siempre que no la haya retirado de la Unidad Academica.


Documento: 8
Articulo: 19
Capitulo: III - INSCRIPCION

Cierre de Inscripcion: En la fecha y hora de vencimiento del plazo deinscripcion, se labrara un acta donde constaran las inscripciones realizadas en el llamado a Concurso la cual sera refrendada por dos funcionarios de mayor jerarquia que se encuentren en la Unidad Academica.


Documento: 8
Articulo: 20
Capitulo: III - INSCRIPCION

Exhibicion de la nomina de aspirantes: Dentro de las cuarenta y ocho (48) horas de la fecha de cierre de la inscripcion, el Decano dispondra la exhibicion en las carteleras murales y difundira en la pagina electronica y por otros medios al alcance de la Facultad la nomina de los aspirantes inscriptos. Tambien, dentro de dicho lapso, la misma debera elevarse a Rectorado y remitirse sin formalidades a los interesados, al domicilio constituido. Dicha publicacion debera realizarse por el termino de cinco (5) dias. RESOLUCION No289/08.


Documento: 8
Articulo: 21
Capitulo: IV - IMPUGNACION DEL ASPIRANTE

Impugnacion de los aspirantes: Durante los cinco (5) dias posteriores al vencimiento de la exhibicion de la nomina de inscriptos, los docentes de la UADER o de otras Universidades Nacionales o Provinciales, los aspirantes, las asociaciones de estudiantes y de graduados reconocidas y las asociaciones cientificas y de profesionales podran ejercer el derecho de impugnar la participacion en el Concurso de los aspirantes inscriptos, la impugnacion solo podra fundarse en: - El que haya sido condenado por delito doloso, mientras dure la sancion. - El condenado por delito cometido en perjuicio de o contra la Administracion Publica Nacional, Provincial o Municipal, mientras dure la sancion. - El condenado por delito contra el orden constitucional, de conformidad al Codigo Penal vigente (Ley N 23.077). - El inhabilitado por sentencia judicial para el ejercicio de cargos publicos, mientras dure la inhabilitacion. - El sancionado por exoneracion en el ambito nacional, provincial o municipal, mientras no sea rehabilitado. - El que tenga proceso penal pendiente que pueda dar lugar a condena por alguno de los delitos enunciados en los apartados 1, 2 y 4 del presente inciso. - El aprovechamiento de la labor intelectual ajena, sin la mencion de quienes la realizaron, aunque sea por encargo y bajo la supervision del que aprovecha de esas tareas. - Haber observado una conducta que importe colaboracion y/o tolerancia complice con actitudes opuestas a los principios de la Constitucion Nacional, al respeto por los Derechos Humanos, a las instituciones democraticas y/o a los principios del pluralismo ideologico y la libertad academica, cuando por el cargo o la funcion deberia oponerse o denunciar las irregularidades cometidas. Sera causal de nulidad absoluta el incumplimiento de cualquiera de los requisitos establecidos de idoneidad moral y civica, por haber tenido una conducta contraria a las instituciones democraticas consagradas por la Constitucion Nacional y/o a los intereses de la Nacion. Se tendra en cuenta para evaluar la procedencia de la impugnacion, si quienes son objetados han ejercido, durante gobiernos no elegidos conforme a lo establecido por la Constitucion Nacional, cargos en instituciones u organismos estatales, nacionales, provinciales o municipales. La objecion debera ser explicitamente fundada y ofrecidas las pruebas que se hicieran valer.


Documento: 8
Articulo: 22
Capitulo: IV - IMPUGNACION DEL ASPIRANTE

La interposicion de la impugnacion suspendera el tramite del Concurso hasta que recaiga resolucion definitiva en el ambito de la Universidad. Dentro de los cinco (5) dias de presentadas, el Decano dara vista de la objecion al aspirante objetado para que formule su descargo. Este debera hacerse por escrito dentro de los cinco (5) dias de comunicada la objecion.


Documento: 8
Articulo: 23
Capitulo: IV - IMPUGNACION DEL ASPIRANTE

Cuando existieran pruebas que acrediten hechos o actos contrarios a la etica universitaria imputables al objetado y tomando en cuenta las actuaciones referentes a la objecion y todo otro antecedente debidamente documentado que estime pertinente o de interes, el Consejo Directivo excluira del Concurso al aspirante objetado. La resolucion que recaiga sobre la objecion, debera dictarse dentro de los cinco (5) dias siguientes de recibido el descargo o de vencido el plazo para presentarlo y sera notificada a las partes dentro de los cinco (5) dias siguientes. Estas podran apelar dentro de los cinco (5) dias de recibida la notificacion ante el Consejo Superior, el que resolvera definitivamente sobre la cuestion, en un plazo no mayor de cuarenta y cinco (45) dias de recibidas las actuaciones correspondientes.


Documento: 8
Articulo: 24
Capitulo: IV - IMPUGNACION DEL ASPIRANTE

Recayendo resolucion definitiva que acoja la objecion invocada, el aspirante sera eliminado de la nomina respectiva. La interposicion de cualquier recurso administrativo o accion judicial a la decision del Consejo Superior no suspendera el tramite del Concurso, pero condicionara sus resultados, sin responsabilidad de la Universidad con respecto a una eventual nulidad de la designacion por anulacion del Concurso.


Documento: 8
Articulo: 25
Capitulo: V - DESIGNACION DEL JURADO

Designacion del Jurado: Los integrantes del Jurado seran designados por el Consejo Directivo de la Facultad que tramita el Concurso, por mayoria absoluta de los miembros presentes, a propuesta del Decano de la Unidad Academica respectiva. Dicha propuesta debera contener mencion sintetizada de sus antecedentes y se efectuara dentro de los ocho (8) dias de cerrada la inscripcion. No podran integrar el Jurado las personas enunciadas en el Art. 14 segundo parrafo.


Documento: 8
Articulo: 26
Capitulo: V - DESIGNACION DEL JURADO

Composicion del Jurado: Los Jurados de cada Concurso estaran compuestos por: a) Tres (3) docentes titulares y dos (2) suplentes. b) Un (1) estudiante titular y un (1) suplente. c) Un (1) graduado titular y un (1) suplente. Los suplentes sustituiran a los titulares por su orden en caso de recusacion, excusacion, renuncia, fallecimiento o remocion, mediante resolucion dictada por el Decano, quien debera comunicarla al Consejo Directivo.


Documento: 8
Articulo: 27
Capitulo: V - DESIGNACION DEL JURADO

Los integrantes del Jurado deberan reunir las siguientes condiciones: Los docentes: a) Ser o haber sido profesor por concurso de categoria no inferior a la del cargo en concurso, habiendo accedido a este por concurso publico y abierto de antecedentes y oposicion. b) Por lo menos dos (2) titulares del Jurado deberan pertenecer o haber pertenecido a otras Universidades Nacionales y/o Provinciales. De sus tres miembros titulares, unicamente uno de ellos podra pertenecer a la UADER. c) Poseer versacion reconocida en el area del conocimiento especifico o tecnico, motivo del Concurso. Los estudiantes: a) Ser alumno regular de la Unidad Academica en cuestion. b) Haber aprobado la materia en Concurso. c) Tener aprobada como minimo la mitad de la carrera.


Documento: 8
Articulo: 28
Capitulo: V - DESIGNACION DEL JURADO

Dentro de los cinco (5) dias de designados los Jurados, se debera notificar fehacientemente a sus integrantes y a los aspirantes. Posteriormente a dicha notificacion se dara a publicidad, la nomina de los miembros que componen el Jurado en la cartelera mural de la Unidad Academica correspondiente y en su pagina electronica, durante ocho (8) dias.


Documento: 8
Articulo: 29
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Recusacion de los miembros del Jurado: Los miembros del Jurado podran ser recusados por escrito, con causa fundada, por los aspirantes dentro de los cinco (5) dias siguientes a la notificacion prevista en el articulo 25 de este Reglamento.


Documento: 8
Articulo: 30
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Causales de recusacion: Seran causales de recusacion: a) El parentesco por con sanguinidad dentro del cuarto grado y segundo de afinidad entre Jurado y algun aspirante. b) Tener el Jurado o sus consanguineos y/o afines, dentro de los grados establecidos en el inciso anterior sociedad o comunidad con alguno de los aspirantes, salvo que la Sociedad fuese anonima. c) Tener algun Jurado miembro pleito pendiente con el aspirante. d) Ser el Jurado o aspirante, reciprocamente, acreedor, deudor o fiador. e) Ser o haber sido el Jurado autor de denuncia o quer ella contra el aspirante, o denunciado o querellado por este ante los Tribunales de Justicia o Tribunal Academico con anterioridad a la designacion del Jurado. f) Haber emitido el Jurado opinion, dictamen o recomendacion prejuzgando acerca del resultado del concurso que se tramita. g) Tener el Jurado amistad intima con alguno de los aspirantes o enemistad o resentimiento que se manifiesten por hechos conocidos en el momento de su designacion. RESOLUCION No289/08. h) Haber recibido el Jurado importantes beneficios del aspirante. i) Carecer el Jurado de versacion reconocida en el area del conocimiento cientifico o tecnico motivo del Concurso. j) Las mencionadas en el articulo 18.


Documento: 8
Articulo: 31
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Excusacion del Jurado: Todo miembro de un jurado que se hallase comprendido en algunas de las causales de recusacion mencionadas en el articulo anterior, debera excusarse.


Documento: 8
Articulo: 32
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Procedimiento: Dentro de los tres (3) dias de la presentacion de la recusacion contra los miembros del Jurado con causa fundada, acompanada por las pruebas que se hicieran valer, el Decano le dara traslado al recusado para que en el plazo de cinco (5) dias presente su descargo y ofrezca las pruebas de que se hiciere valer. El Decano procedera a la recepcion de las pruebas ofrecidas en un periodo que no podra exceder de ocho (8) dias. El numero de testigos se limita a tres (3).


Documento: 8
Articulo: 33
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Las recusaciones y excusaciones de los miembros del Jurado seran resueltas directamente por el Consejo Directivo. Con tal fin el Decano elevara las actuaciones dentro de los cinco (5) dias de haberse formulado las excusaciones o de haberse presentado los descargos en el caso de las recusaciones o de haber concluido la recepcion de las pruebas. El Consejo Directivo resolvera definitivamente, dentro de los doce (12) dias de recibidas las actuaciones correspondientes.


Documento: 8
Articulo: 34
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

De aceptarse la recusacion o la excusacion, el miembro del Jurado separado sera reemplazado por el miembro suplente que sigue en el ordende designacion.


Documento: 8
Articulo: 35
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Los Jurados podran hacerse representar en los tramites de las recusaciones y excusaciones, de acuerdo a lo previsto en el Art. 14 del presente Reglamento.


Documento: 8
Articulo: 36
Capitulo: VI - RECUSACION DE LOS MIEMBROS DEL JURADO

Cuando un aspirante objetado hubiera formulado recusacion contra algun miembro del Jurado, el tramite de esta ultima quedara suspendido hasta tanto quede resuelta la objecion.


Documento: 8
Articulo: 37
Capitulo: VII - ACTUACION DEL JURADO

Constitucion miembros del Jurado: Una vez vencidos los plazos para las recusaciones, excusaciones o impugnaciones o cuando ellas hubieran quedado resueltas con caracter definitivo, el Decano remitira al Jurado copia del acta de cierre, en la cual consta la nomina de aspirantes. La planilla de inscripcion, con mencion de los antecedentes y el sobre cerrado conteniendo la planificacion de catedra, sera enviada a los miembros del Jurado por la oficina de concurso, quienes podran requerir a los aspirantes, por intermedio de la misma oficina, las aclaraciones o informaciones complementarias. Las actuaciones de las impugnaciones, recusaciones y excusaciones no quedaran incorporadas al expediente del Concurso, pero debera dejarse constancia en el mismo a donde fueron remitidas para su archivo. RESOLUCION No289/08.


Documento: 8
Articulo: 38
Capitulo: VII - ACTUACION DEL JURADO

Dentro de los diez (10) dias corridos de la notificacion de la copia referida en el articulo  anterior, el Decano - previa consulta con los miembros del Jurado - fijara por Resolucion: a) Fecha y hora de reunion del Jurado a fin de proceder a la evaluacion de los antecedentes, la cual debera realizarse dentro de los veinte (20) dias corridos de enviada la copia de la nomina de aspirantes. b) Fecha y hora de la clase publica, y de la entrevista o en su defecto facultar al Responsable de la Oficina de Concursos a fijar una nueva fecha a solicitud fundada del Jurado, quedando bajo su competencia poner en conocimiento de todos los actuantes esta novedad.


Documento: 8
Articulo: 39
Capitulo: VII - ACTUACION DEL JURADO

El jurado funcionara validamente con la presencia de los tres (3) miembros academicos y al menos uno (1) de los representantes de los otros claustros.


Documento: 8
Articulo: 40
Capitulo: VII - ACTUACION DEL JURADO

Sorteo del tema y orden de exposicion: Cada miembro del Jurado - estamento docente - seleccionara tres temas del programa vigente de la materia a concursar en la Unidad Academica, de acuerdo a la modalidad especificada por la Facultad, ya sea catedras, areas, nucleos, asignaturas que integran los nucleos, disciplina, laboratorio y lo remitira a la misma en sendos sobres cerrados para su posterior sorteo. El sorteo se llevara acabo con una antelacion de cuarenta y ocho (48) horas respecto de la fecha y hora fijada en el articulo 35o- Inc. b) en acto publico, en el que estara presente el Decano y/o un (1) miembro del Consejo Superior o Directivo y/o un (1) miembro del Jurado, asi como los concursantes que lo deseen y quienes asistan al acto. A tal efecto se requerira la notificacion fehaciente del acto a los postulantes con una anticipacion minima de cuarenta y ocho (48) horas. El sorteo se hara con un minimo de seis (6) sobres. En el supuesto caso de no alcanzar el numero minimo de sobres arriba exigidos, se prorrogara la clase publica por un plazo de hasta treinta (30) dias. El Decano debera fijar la nueva fecha y comunicarla a los aspirantes y a los Jurados. Los sobres recibidos se reservaran y se solicitara la remision a los miembros del tribunal que no los hayan hecho llegar, a fin de cumplir con lo exigido para proceder al sorteo. A posteriori del sorteo se dara a conocer el contenido de los restantes sobres presentados. Se debera sortear tambien el orden en que expondran los concursantes. El tema sera el mismopara todos los aspirantes al cargo motivo del Concurso.


Documento: 8
Articulo: 41
Capitulo: VII - ACTUACION DEL JURADO

El Jurado debera tomar una prueba de oposicion ajustada a las siguientesreglas: a) Sera publica a excepcion de los propios concursantes, quienes no podran escuchar las exposiciones de los otros participantes. b) Sera oral y debera tener caracter academico universitario y estar adecuada a la comprension y nivel de los alumnos que atendera el aspirante en el caso de ser seleccionado. c) Se valoraran en ella los contenidos expuestos y la capacidad didactica del aspirante. d) No podra consistir en una mera lectura, permitiendoseles solo la consulta de guias de exposicion. e) Tendra una duracion no superior a cuarenta y cinco (45) minutos. f) Debera desarrollarse con la presencia de la totalidad de los miembros del Jurado. g) Durante su transcurso, los disertantes no podran ser interrogados ni interrumpidos. h) Concluida la clase, se podra requerir a los concursantes las aclaraciones pertinentes. RESOLUCION No289/08


Documento: 8
Articulo: 42
Capitulo: VII - ACTUACION DEL JURADO

Los miembros del Jurado en forma conjunta deberan entrevistarse personalmente con cada uno de los aspirantes para completar el juicio sobre la capacidad docente y dedicacion de los concursantes, valorar su motivacion docente, la forma en que ha desarrollado, desarrolla y eventualmente desarrollara la ensenanza, los puntos de vista sobre los temas basicos de su campo de conocimiento que deban transmitirse a los alumnos, los medios que propone para mantener actualizada la ensenanza, y llevar a la practica los cambios que sugiere, asi como sus planes de investigacion y trabajo y cualquier otra informacion, que a juicio de los miembros del Jurado, sea conveniente requerir.


Documento: 8
Articulo: 43
Capitulo: VII - ACTUACION DEL JURADO

Las autoridades de la Unidad Academica respectiva seran responsables de notificar fehacientemente a los aspirantes la fecha y hora que se haya dispuesto para la entrevista con cada postulante y para la o las pruebas de oposicion.


Documento: 8
Articulo: 44
Capitulo: VII - ACTUACION DEL JURADO

Pautas para la evaluacion: Sobre un total de cien (100) puntos, el Jurado podra otorgar al aspirante un maximo de cuarenta (40) puntos en lo concerniente a los antecedentes, un maximo de treinta (30) puntos en lo que se refiere a la oposicion y un maximo de treinta (30) para la entrevista personal.


Documento: 8
Articulo: 45
Capitulo: VII - ACTUACION DEL JURADO

Evaluacion de la oposicion: En la evaluacion de la entrevista que versara sobre los puntos establecidos en el Articulo 11, y de la clase publica se deberan tener preferentemente en cuenta, segun el cargo concursado, la claridad y orden expositivo de los aspirantes, asi como el grado de actualizacion informativa en relacion con los demas temas considerados.


Documento: 8
Articulo: 46
Capitulo: VII - ACTUACION DEL JURADO

Participara en las deliberaciones del Jurado, un (1) docente designado por el Consejo Directivo, quien debera pertenecer a la Unidad Academica en cuestion, y no tendra voto pero si voz, y fundara por escrito las observaciones que considere convenientes, las cuales deberan ser agregadas al expediente del concurso. Su  participacion se remitira exclusivamente a considerar los aspectos formales administrativos del Acto del Concurso.


Documento: 8
Articulo: 47
Capitulo: VII - ACTUACION DEL JURADO

El Jurado estudiantil emitira dictamen sobre los aspectos pedagogicos didacticos desarrollados por el aspirante en la clase publica y el Jurado graduado emitira dictamen sobre la vinculacion que logro establecer el aspirante entre su propuesta de ensenanza y el ejercicio profesional.


Documento: 8
Articulo: 48
Capitulo: VII - ACTUACION DEL JURADO

Dictamen Final: Substanciada la prueba, dentro de los cinco (5) dias posteriores el Jurado debera elevar al Consejo Directivo, inexcusablemente un orden de merito para cada cargo y/o dedicacion entre los aspirantes o postulantes evaluados. No podra considerar a dos o mas de ellos en igualdad de meritos y debera contener: 1- La justificacion debidamente fundada de las exclusiones de aspirantes al Concurso. 2- La nomina de los aspirantes que posean antecedentes de autentica jerarquia. 3- El detalle y valoracion de: a- Los titulos y antecedentes. b- Publicaciones, trabajos cientificos y academicos. c- Prueba de oposicion. d- Entrevista personal y plan de trabajo (docente, de investigacion, de extension). e- Demas elementos de juicio considerados. 4- El orden de meritos para el o los cargos o funciones objeto del Concurso, nomina que sera encabezada por los aspirantes propuestos como candidatos para ocupar el/los cargo/s motivo del Concurso, y continuado por el resto de los aspirantes considerados en el orden de meritos. En el caso de haberse especificado mas de una categoria y/o dedicacion, el Jurado se expedira sobre estos puntos, por separado. Si no existiera unanimidad se elevaran tantos dictamenes como posiciones existieran.


Documento: 8
Articulo: 49
Capitulo: VIII - RESOLUCION DEL CONCURSO

Notificacion del Dictamen Jurado: Las conclusiones del Dictamen del Jurado, deberan ser notificadas a los aspirantes dentro de los tres (3) dias de emitidos poniendose a disposicion de los mismos todos los actuados que permaneceran en las respectivas Unidades Academicas y seran impugnables por defectos de forma o procedimiento asi como por manifiesta arbitrariedad, dentro de los cinco (5) dias de la notificacion. Este recurso debera interponerse y fundarse por escrito ante el Consejo Directivo.


Documento: 8
Articulo: 50
Capitulo: VIII - RESOLUCION DEL CONCURSO

Dentro de los treinta (30) dias de haberse expedido el Jurado y sobre la base de su dictamen, de las observaciones formuladas por los participantes mencionados en el Articulo 44 y, de las impugnaciones que hubieran formulado los aspirantes, las cuales quedaran resueltas con asesoramiento legal si correspondiere, el Consejo Directivo, expresando los fundamentos podra: A) Solicitar al Jurado la ampliacion o aclaracion del dictamen, en cuyo caso aquel debera expedirse dentro de los ocho (8) dias de tomar conocimiento de la solicitud. B) Proponer al Consejo Superior declarar desierto el Concurso. C) Proponer al Consejo Superior dejar sin efecto el Concurso y llamar uno nuevo. D) Aprobar el Concurso y elevarlo al Consejo Superior con las siguientes posibilidades: 1. Proponer al aspirante ubicado en primer termino del dictamen unico o alguno de los dictamenes del Jurado. 2. Proponer en forma alternativa para cubrir el/los cargo/s a dos (2) aspirantes ubicados en el primer y segundo termino del orden de merito del dictamen o algunos de los dictamenes del Jurado. Para los llamados a Concurso para cubrir mas de un (1) cargo realizado de acuerdo al Articulo 58 de este Reglamento, podra proponer a los aspirantes respetando el orden de merito elaborado del Jurado conforme a las pautas del parrafo anterior.


Documento: 8
Articulo: 51
Capitulo: VIII - RESOLUCION DEL CONCURSO

La resolucion recaida sobre el Concurso sera comunicada a los aspirantes quienes dentro de los cinco (5) dias posteriores podran impugnar lo dispuesto por el Consejo Directivo, mediante escrito presentado al Decano fundado en defectos de forma o de procedimiento, asi como por manifiesta arbitrariedad. Cumplido el termino establecido precedentemente, las actuaciones del Concurso y el recurso, si lo hubiera, seran elevadas al Consejo Superior.


Documento: 8
Articulo: 52
Capitulo: VIII - RESOLUCION DEL CONCURSO

El Consejo Superior podra solicitar aclaraciones sobre la o las propuestas del Consejo Directivo, en cuyo caso este debera expedirse dentro de los quince (15) dias de tomar conocimiento de la solicitud. En un plazo no mayor de veinticuatro (24) dias de recibida la propuesta y/o las aclaraciones de dicho organo, podra aceptar la propuesta del Consejo Directivo, o rechazarla. Si la propuesta fuera rechazada el Concurso quedara sin efecto. Dicha resolucion se notificara a los interesados y sera difundida a traves de las carteleras murales y de la pagina electronica de la Unidad Academica correspondiente. En los Concursos en los que no se formulen propuestas para la totalidad de los cargos concursados, los que no se provean seran declarados desiertos.


Documento: 8
Articulo: 53
Capitulo: VIII - RESOLUCION DEL CONCURSO

En caso de que el Jurado hubiere recomendado la designacion de un aspirante en una categoria distinta a la del llamado respectivo y si dentro del plazo de un (1) ano se volviere a llamar a Concurso en tal categoria y asignatura y no se registrasen otras inscripciones para el cargo, el Consejo Superior  a propuesta del Consejo Directivo - podra efectuar la pertinente designacion sobre la base del dictamen de Concurso anterior.


Documento: 8
Articulo: 54
Capitulo: IX - DESIGNACION DE PROFESORES

La designacion de profesores por Concurso estara a cargo del Consejo Superior de acuerdo a lo estipulado en el Articulo 49 de este Reglamento.


Documento: 8
Articulo: 55
Capitulo: IX - DESIGNACION DE PROFESORES

Notificado de su designacion, el profesor debera asumir sus funciones dentro de los treinta (30) dias, salvo que invocare ante el Decano un impedimento justificado. En tal caso, el Consejo Directivo la extendera por un plazo no mayor a treinta (30) dias y por unica vez. Transcurrido ese plazo o vencida la prorroga acordada si el profesor no se hiciera cargo de sus funciones, el Consejo Directivo debera poner el hecho en conocimiento del Consejo Superior para que este deje sin efecto la designacion.


Documento: 8
Articulo: 56
Capitulo: IX - DESIGNACION DE PROFESORES

Si la designacion quedara sin efecto por las razones mencionadas en el articulo anterior, el profesor quedara inhabilitado para presentarse a Concurso o ejercer cualquier cargo docente en esta Universidad por el plazo de tres (3) anos a partir de la fecha en que debio asumir sus funciones. No procedera esta sancion cuando el profesor renuncie por haber optado por otro cargo ganado en concurso o mediar causa suficiente a juicio del Consejo Superior. La misma sancion correspondera a los profesores que una vez designados permanezcan en sus cargos por un lapso menor de dos anos sin invocar causa justificada a juicio del mismo organo. Este articulo se incluira en la notificacion de la designacion. Dentro de los doce (12) meses de vencido el plazo de inscripcion en un Concurso para la designacion de profesores por concurso, si por cualquier razon el cargo no fue aceptado o quedara vacante, el Consejo Directivo podra retrotraer el procedimiento para la designacion en la catedra respectiva, a la etapa prevista en el articulo 47 de este Reglamento.


Documento: 8
Articulo: 57
Capitulo: IX - DESIGNACION DE PROFESORES

Las designaciones de Profesores titulares, asociados y adjuntos resultantes de los concursos de catedras, areas, nucleos, asignaturas que integran los nucleos, disciplinas, laboratorio no implican la consolidacion de la asignacion de dichos cargos en la unidad pedagogica concursada (catedra, departamento, etc.). Dicha designacion dependera de eventuales modificaciones de los planes de estudios, reorganizacion de la Unidad Academica y otras razones que decida la Universidad.


Documento: 8
Articulo: 58
Capitulo: X - NORMAS GENERALES

La inscripcion al Concurso importara para el aspirante su conformidad con las normas de este Reglamento y las especificas dictadas por cada Unidad Academica.


Documento: 8
Articulo: 59
Capitulo: X - NORMAS GENERALES

Si el Rector, el Vicerrector, los Decanos y los Secretarios de la Universidad o de las Unidades Academicas, desempenan cargos de Profesor por concurso o interino, el llamado a concurso podra ser suspendido o diferido, hasta tanto permanezcan en sus funciones. Una vez concluidas sus funciones se reabrira el llamado a Concurso para esos cargos debiendo transcurrir un plazo equivalente del que desempeno sus funciones, el que no podra exceder de cuatro (4) anos.


Documento: 8
Articulo: 60
Capitulo: X - NORMAS GENERALES

Las notificaciones que deban efectuarse a los aspirantes se realizaran mediante cedula, personalmente, por carta documento o por telegrama colacionado, en el domicilio que deberan constituir conforme con lo dispuesto en el articulo 9 inciso 1) de este Reglamento.


Documento: 8
Articulo: 61
Capitulo: X - NORMAS GENERALES

Los llamados a Concurso, se haran dentro de lo posible para una catedra, area, nucleo, asignaturas que integran los nucleos, disciplina, laboratorio, pero no para los cursos en que estos estuvieran divididos, pudiendo cada Facultad adaptar lo aqui dispuesto a su estructura academica.


Documento: 8
Articulo: 62
Capitulo: X - NORMAS GENERALES

Cuando existan reales dificultades para obtener miembros de los Jurados, el Consejo Directivo excepcionalmente podra autorizar a prescindir de la exigencia del Articulo 24 inciso a) designandose personalidades reconocidas que deberan reunir el requisito del inciso c) del mismo apartado y articulo, evidenciado por una actividad profesional relevante, publicaciones, etc. Ante la existencia de dificultades en el momento de sustanciarse el concurso, le permitira aumentar en uno (1) el numero de Jurados que pertenezcan a la Universidad.


Documento: 8
Articulo: 63
Capitulo: X - NORMAS GENERALES

Lo dispuesto en los articulos 24 y 59 no excluye que las designaciones recaigan en universitarios extranjeros.


Documento: 8
Articulo: 64
Capitulo: X - NORMAS GENERALES

Plazos: Todos los plazos establecidos en este Reglamento, salvo disposicion expresa que indique lo contrario, se computaran como dias habiles administrativos y seran perentorios.


Documento: 8
Articulo: 65
Capitulo: XI - NORMAS TRANSITORIAS

Hasta que no se haya completado el dictado de todas las asignaturas que corresponden a los distintos planes de estudios, los Jurados alumnos deberan tener regularizadas el 70% de las materias hasta el ano al que corresponde la materia donde se concursara el cargo y haber aprobado la misma. Para efectuar la seleccion del Jurado alumno, los Consejeros Estudiantiles, presentaran al Consejo Consultivo la nomina de aquellos que reunan las condiciones exigidas en el presente articulo.


Documento: 8
Articulo: 66
Capitulo: XI - NORMAS TRANSITORIAS

Los graduados, para la integracion de los Jurados de Concurso, deberan ser tomados del padron de egresados (de la carrera) reconocido. De no poder integrarse el miembro determinado en el inciso c) del Articulo 23 del Regimen de Concurso para cada Jurado, este funcionara validamente.


Documento: 9
Articulo: 67
Capitulo: 

Deroguese la Res. 141/03 del 1o de agosto de 2003.


Documento: 9
Articulo: 68
Capitulo: 

Apruebese el Reglamento de Concurso docente de Antecedentes con Presentacion de Proyectos para la provision de cargos docentes interinos, el que regira para la cobertura de espacios curriculares en las distintas carreras que se cursan en esta Facultad, y cuyo texto pasa a formar parte de la presente como Anexo Unico.


Documento: 9
Articulo: 69
Capitulo: 

Registrese, comuniquese, notifiquese a la parte interesada y oportunamente archivese.


Documento: 9
Articulo: 70
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Producida una vacante o la necesidad de cubrir un espacio curricular nuevo, se dispondra el llamado abierto a un registro de aspirantes para cubrir las horas catedra o el cargo correspondiente con caracter de interino.


Documento: 9
Articulo: 71
Capitulo: Reglamento de Concurso Docentes de Antecedentes

La difusion del mismo se efectuara a traves de los medios escritos de circulacion masiva en la zona de influencia de la subsede, y en cada una de las unidades academicas interesadas. Se informara sobre: 2.1 Cargo o funcion a concursar. 2.2 Fecha de apertura y cierre de la inscripcion. 2.3 Lugar de inscripcion y horario de atencion.


Documento: 9
Articulo: 72
Capitulo: Reglamento de Concurso Docentes de Antecedentes

El periodo de inscripcion debera comprender cinco (5) dias habiles posteriores a la publicacion.


Documento: 9
Articulo: 73
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Las solicitudes de inscripcion se formalizaran por nota dirigida al Decano, tendran caracter de declaracion jurada y seran presentadas por los aspirantes o personas autorizadas por estos, en sede o subsede de la Facultad que corresponda, en tres (3) ejemplares, bajo recibo en el que constara la fecha de recepcion, con la informacion basica siguiente: 4.1 Apellido y nombres, nacionalidad, estado civil, fecha y lugar de nacimiento, domicilio real, clase y numero de documento. 4.2 Titulos con la indicacion de la institucion que los otorgo. 4.3 La totalidad de los antecedentes docentes (actuacion en universidades y Facultades nacionales, provinciales y/o privados registrados en el pais o en el extranjero) y los no docentes (cargos desempenados en la administracion publica o en la actividad privada) e indole de las tareas desarrolladas, indicando la institucion, el periodo de ejercicio y la naturaleza de la designacion. 4.4 Nomina de obras y publicaciones realizadas por el aspirante, consignando la editorial o revista y el lugar y fecha de publicacion. Se podra exigir que se presenten copias de las publicaciones y los trabajos mencionados las que seran devueltas una vez efectuada la evaluacion de los antecedentes. 4.5 Otros antecedentes relacionados con la especialidad tales como: cursos realizados, cursos y conferencias dictados, etc. 4.6 Participacion en Congresos y/o Jornadas nacionales y/o internacionales. 4.7 Distinciones, premios y becas obtenidos.


Documento: 9
Articulo: 74
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Los aspirantes deberan adjuntar la documentacion que acredite los antecedentes invocados en su presentacion, en original o en copia legalizada. Esta documentacion debera presentarse debidamente foliada, podra ser completada hasta tres (3) dias despues del cierre de la inscripcion pero en ningun caso se aceptara documentacion fuera de este termino suplementario. La misma podra ser retirada de la Facultad una vez realizada la evaluacion de antecedentes o cuando ocurra desistimiento del aspirante.


Documento: 9
Articulo: 75
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Las carpetas de antecedentes seran elevadas por Bedelia al Decano de la Facultad quien dispondra sin mas tramite la devolucion de las presentaciones que no se ajusten a lo establecido en este reglamento.


Documento: 9
Articulo: 76
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Juntamente con la solicitud de inscripcion, los aspirantes deberan presentar un trabajo de planeamiento de catedra en el que se expidan sobre la insercion de la asignatura en el Plan de Estudio, programa de la asignatura, criterios, evaluaciones, estrategias didacticas, bibliografia, organizacion de la Catedra, y cuando sea aplicable, investigacion y extension. El trabajo requerido debera presentarse en tres (3) ejemplares, en sendos sobres cerrados.


Documento: 9
Articulo: 77
Capitulo: Reglamento de Concurso Docentes de Antecedentes

En la fecha y hora de cierre de la inscripcion se labrara un Acta donde consten las inscripciones realizadas en el llamado a Concurso la cual sera refrendada por los dos funcionarios de mayor jerarquia que se encuentren en la Facultad.


Documento: 9
Articulo: 78
Capitulo: Reglamento de Concurso Docentes de Antecedentes

El Decano, designara por Resolucion, el Jurado que intervendra en la evaluacion de antecedentes. La misma sera integrada por: 9.1 Tres docentes titulares y dos suplentes. 9.2 Un veedor para verificar procedimientos, representante del gremio.


Documento: 9
Articulo: 79
Capitulo: Reglamento de Concurso Docentes de Antecedentes

La constitucion del mismo permanecera expuesta durante tres (3) dias habiles en los transparentes de la Facultad.


Documento: 9
Articulo: 80
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Los miembros del Jurado podran ser recusados por los aspirantes, por escrito, con causa fundada, dentro de los dos (2) dias posteriores al plazo de exhibicion de la nomina.


Documento: 9
Articulo: 81
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Seran causales de recusacion: 12.1 El matrimonio, o parentesco por consanguinidad hasta cuarto grado o afinidad hasta segundo grado entre algun miembro del Jurado y algun aspirante. 12.2 La amistad o enemistad manifiesta entre algun miembro del Jurado y algun aspirante. 12.3 El interes directo de algun miembro del Jurado en el resultado del Concurso.


Documento: 9
Articulo: 82
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Todo miembro del Jurado que se encontrase comprendido en alguna de las causales de recusacion mencionadas en el articulo anterior, debera excusarse indefectiblemente.


Documento: 9
Articulo: 83
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Dentro de los tres dias de la presentacion de la recusacion contra algun miembro del Jurado, el Decano, previa confrontacion, le dara traslado al recusado para que en el plazo de tres (3) dias habiles presente su descargo.


Documento: 9
Articulo: 84
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Las recusaciones y excusaciones de los miembros del Jurado seran resueltas directamente por el Decano en base a las actuaciones, los descargos y pruebas recepcionadas.


Documento: 9
Articulo: 85
Capitulo: Reglamento de Concurso Docentes de Antecedentes

De aceptarse la recusacion, el miembro del Jurado, objeto de la impugnacion, sera reemplazado por los suplentes siguiendo el orden de la designacion.


Documento: 9
Articulo: 86
Capitulo: Reglamento de Concurso Docentes de Antecedentes

El Jurado presentara al Decano su dictamen que constara en un Acta firmada por todos sus integrantes y debera contener el orden de merito para cubrir el cargo objeto del llamado y la fundamentacion resultante del analisis de los antecedentes. El Jurado tomara para la evaluacion de los antecedentes los siguientes parametros de evaluacion:  Titulo (Hasta 15 puntos).  Docencia (Antiguedad, niveles educativos de desempeno, formas de designacion, otras tareas docentes como formacion de Recursos Humanos, direcciones de tesis, etc.) (Hasta 15 puntos).  Actualizacion, perfeccionamiento en la catedra objeto de concurso y perfeccionamiento (Hasta 15 puntos).  Produccion (cientifica, profesional, docente, etc) (Hasta 15 puntos). Para la evaluacion del Planeamiento de catedra se asignara un puntaje entre 0 y 40, el que se sumara con el puntaje obtenido por los antecedentes. El jurado estara facultado para solicitar una entrevista con el /los aspirantes en caso que lo considere pertinente. Si no existiera unanimidad deberan elevarse tantos dictamenes como posiciones existieren. En caso de que el Jurado lo considere adecuado, podra proponer con la debida fundamentacion, declarar desierto el Concurso. Si el Decano considera insuficiente los fundamentos del dictamen podra solicitar ampliacion del mismo al Jurado.


Documento: 9
Articulo: 87
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Las listas resultantes seran publicadas en la Facultad por el termino de tres (3) dias. Vencido este plazo podran presentarse impugnaciones durante los dos (2) dias subsiguientes. Las mismas seran tratadas y resueltas por el Decano en el termino de quince (15) dias.


Documento: 9
Articulo: 88
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Si el dictamen del Jurado incluye un orden de meritos, el mismo mantendra su sugerencia por el termino de un (1) ano, debiendo recurrirse a el si se produce una nueva vacante o pedido de licencia.


Documento: 9
Articulo: 89
Capitulo: Reglamento de Concurso Docentes de Antecedentes

En caso de solicitudes de licencia que no superen los sesenta (60) dias y que no existiera un orden de merito vigente el Decano nombrara a propuesta de los Responsables de carrera a un docente en forma directa.


Documento: 9
Articulo: 90
Capitulo: Reglamento de Concurso Docentes de Antecedentes

El Decano evaluara el dictamen propuesto por el Jurado y previa ratificacion por parte del postulante de su interes en cubrir el cargo, se elevara la propuesta a la U.A.D.E.R..


Documento: 9
Articulo: 91
Capitulo: Reglamento de Concurso Docentes de Antecedentes

Cualquier otra situacion no prevista en la presente reglamentacion sera tratada y resuelta por el Decano.


Documento: 5
Articulo: 92
Capitulo: 

Apruebese el Reglamento Academico de la Facultad de Ciencia y Tecnologia de la Universidad Autonoma de Entre Rios, en un todo de acuerdo con el texto que se detalla en su cuerpo principal y en sus Anexos I, II, III y IV.


Documento: 5
Articulo: 93
Capitulo: 

Deroguese toda norma vigente hasta la fecha que se oponga a la presente.


Documento: 5
Articulo: 94
Capitulo: 

Registrese, comuniquese a quienes corresponda, notifiquese a la parte interesada y oportunamente archivese.


Documento: 5
Articulo: 95
Capitulo: I. DISPOSICIONES GENERALES

El presente regimen queda instituido para regular las actividades academicas de pregrado y grado de: a) Los alumnos inscriptos en las distintas carreras de la Facultad de Ciencia y Tecnologia dependiente de la Universidad Autonoma de Entre Rios. b) Los alumnos que se inscriban para cursar una o mas asignaturas en condicion de alumnos vocacionales, segun Art.75 y 80 del Estatuto de la UADER. c) El personal docente de la Facultad de Ciencia y Tecnologia. El personal de las distintas areas y departamentos dependientes de Secretaria Academica de la Facultad de Ciencia y Tecnologia.


Documento: 5
Articulo: 96
Capitulo: I. DISPOSICIONES GENERALES

La presente normativa se aplicara en todas las estructuras academicas - en la sede central, en todas sus subsedes y en las que se crearen - de la Facultad de Ciencia y Tecnologia dependiente de la Universidad Autonoma de Entre Rios, y a todos aquellos actos de docentes, personal y alumnos que se produjeran fuera de la Facultad y pudieren afectarla.


Documento: 5
Articulo: 97
Capitulo: II. DEL INGRESO  

El ingreso de personal docente y de alumnos a esta Facultad, se regulara segun las disposiciones y condiciones que se establezcan oficialmente por parte de la Universidad Autonoma de Entre Rios, para cada periodo lectivo.


Documento: 5
Articulo: 98
Capitulo: III. DEL PERIODO LECTIVO Y ANO ACADEMICO

El ano lectivo se desarrollara en dos periodos que seran determinados anualmente en calendario academico aprobado por el Consejo Directivo de la Facultad. Cada periodo respetara el numero de semanas minimas que establece la Universidad para el dictado de clases.  


Documento: 5
Articulo: 99
Capitulo: III. DEL PERIODO LECTIVO Y ANO ACADEMICO

La Secretaria Academica propondra al Consejo Directivo de la Facultad el calendario academico del ano lectivo siguiente antes de finalizar el 2o cuatrimestre del ano en curso.


Documento: 5
Articulo: 100
Capitulo: III. DEL PERIODO LECTIVO Y ANO ACADEMICO  

Se entiende por ano academico el periodo comprendido entre el 1o de abril de cada ano calendario y el 31 de marzo del ano calendario siguiente.


Documento: 5
Articulo: 101
Capitulo: IV. DE LOS ALUMNOS. CATEGORIAS DE LOS ALUMNOS

La Facultad de Ciencia y Tecnologia reconocera las siguientes categorias de alumnos, atendiendo a su inscripcion al ano academico: *Alumno Activo. *Alumno Pasivo. Sera alumno activo todo aquel que efectue su inscripcion en el ano academico en los periodos que cada ano fije la Facultad. Sera alumno pasivo todo aquel que no efectue su inscripcion en el ano academico en los periodos que cada ano fije la Facultad.


Documento: 5
Articulo: 102
Capitulo: IV. DE LOS ALUMNOS. CATEGORIAS DE LOS ALUMNOS

Todo alumno que se encuentre en la categoria de pasivo en un ano academico no podra realizar ningun tipo de actividad academica (cursar o rendir materias) en dicho ano. Si mantuviera esta categoria durante tres anos consecutivos sera dado de baja como alumno de la Facultad.


Documento: 5
Articulo: 103
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

Los alumnos activos podran revistar en cada asignatura en la condicion de regulares, libres o vocacionales de acuerdo a lo definido en la planificacion de cada catedra.


Documento: 5
Articulo: 104
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

La inscripcion en una asignatura  siempre que se ajuste al regimen de correlatividades establecido en el Plan de Estudios correspondiente - otorga al alumno la posibilidad de acceder a la condicion de regular, que le permite concurrir a clase y participar de todas las actividades inherentes al proceso de ensenanza y de aprendizaje planificadas por la catedra. Tal condicion sera adquirida cuando el alumno cumplimente los requisitos fijados en la planificacion de cada catedra.


Documento: 5
Articulo: 105
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

La regularidad en una asignatura se mantendra hasta transcurridos dos anos academicos posteriores a aquel en el que el alumno obtuvo esa condicion. La regularidad se perdera automaticamente, aun sin haber vencido dicho plazo, si el alumno resultara desaprobado por quinta vez en los turnos de examenes finales.


Documento: 5
Articulo: 106
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

Se admitira la inscripcion de alumnos en asignaturas en las que acrediten la regularidad, lo que implicara automaticamente la perdida de la regularidad acreditada hasta ese momento en esa asignatura. Una vez inscripto nuevamente, el alumno debera satisfacer todos los requisitos establecidos en la planificacion de la respectiva catedra, vigente al momento de la inscripcion, para el cursado de la asignatura.


Documento: 5
Articulo: 107
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

La perdida de la regularidad  en caso de producirse, de acuerdo con lo previsto por la catedra  implica para el alumno el pase a la condicion de alumno libre.


Documento: 5
Articulo: 108
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

La condicion de alumno libre ya sea por perdida de regularidad o por no haber cursado nunca la asignatura, le otorga  siempre que satisfaga los requisitos establecidos en el regimen de correlatividades -  el derecho a rendir examen final, el que debera: *Versar sobre la totalidad de los contenidos de la asignatura; *Ajustarse a lo establecido en la respectiva planificacion, en lo relativo a examenes de alumnos en condicion de libres.


Documento: 5
Articulo: 109
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

Aquel alumno que se inscriba para cursar una o varias asignaturas en carreras de la Facultad sin inscribirse a una determinada carrera sera considerado alumno vocacional. Toda persona que lo solicite sera inscripta como alumno vocacional en cualquier catedra de las carreras de esta Facultad. Podra presentarse a examen y solicitar certificado de curso aprobado. Estos examenes rendidos por alumnos vocacionales no daran opcion a titulo universitario alguno.


Documento: 5
Articulo: 110
Capitulo: IV. DE LOS ALUMNOS. CONDICION DE LOS ALUMNOS Y REGULARIDAD

La inscripcion en una asignatura como alumno vocacional otorga al alumno el derecho a: a) concurrir a clase y  participar en todas las actividades inherentes al proceso de ensenanza y de  aprendizaje planificadas por la catedra; b) acceder al examen final y a una certificacion de aprobacion del curso.


Documento: 5
Articulo: 111
Capitulo: IV. DE LOS ALUMNOS. MATERIAS PRACTICAS

Las materias relativas a la Practica Docente no admitiran alumnos libres.


Documento: 5
Articulo: 112
Capitulo: IV. DE LOS ALUMNOS. MATERIAS PRACTICAS

Las materias eminentemente practicas, como por ejemplo los Laboratorios, no podran considerar la condicion de alumno libre.


Documento: 5
Articulo: 113
Capitulo: IV. DE LOS ALUMNOS. PROMOCION DE UNA ASIGNATURA

El alumno regular podra aprobar la asignatura por promocion directa o por promocion con examen final, segun se establezca en la planificacion de la asignatura. a. Los alumnos promocionados en forma directa, tendran la asignatura aprobada de acuerdo a los requisitos fijados en la planificacion de la catedra, debiendo cumplimentar ademas el Regimen de Correlatividades vigente. b. Los alumnos promocionados con examen final, podran aprobar la asignatura a traves de una instancia final de evaluacion que se llevara a cabo en los turnos de examenes previstos para tal fin en el calendario academico.


Documento: 5
Articulo: 114
Capitulo: IV. DE LOS ALUMNOS. PROMOCION DE UNA ASIGNATURA

El alumno libre podra aprobar la asignatura a traves de un examen final en caracter de libre; o podra reinscribirse nuevamente en la catedra para volver a cursarla.


Documento: 5
Articulo: 115
Capitulo: IV. DE LOS ALUMNOS. PROMOCION DE UNA ASIGNATURA

El docente responsable de cada catedra, elevara al finalizar cada cuatrimestre la planilla de regularidades, donde indicara los alumnos que han regularizado, promocionado en forma directa o que han quedado libres.


Documento: 5
Articulo: 116
Capitulo: IV. DE LOS ALUMNOS. PROMOCION DE UNA ASIGNATURA

Los alumnos promocionados en forma directa, tendran la asignatura aprobada, luego que el Departamento Alumnado, recepcione el acta de evaluacion correspondiente, entregada por los docentes. Dicha acta debera ser entregada dentro de las 48 h posteriores a la finalizacion del cursado de las asignaturas.


Documento: 5
Articulo: 117
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. TURNOS DE EXAMENES

Se habilitaran en cada ano academico cinco turnos de examenes finales: el primero en mayo, con un llamado; el segundo en julio-agosto, con dos llamados; el tercero en septiembre con un llamado, el cuarto en diciembre con dos llamados y el ultimo en febrero-marzo, con dos llamados.


Documento: 5
Articulo: 118
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. TURNOS DE EXAMENES

La instancia final de evaluacion estara a cargo de un tribunal examinador formado por no menos de tres profesores designados a tal efecto, incluyendo al profesor responsable de la asignatura.


Documento: 5
Articulo: 119
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. TURNOS DE EXAMENES

El alumno debera concurrir a los examenes, tanto parciales como finales, con su documento de identidad o libreta universitaria.


Documento: 5
Articulo: 120
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. TURNOS DE EXAMENES

El resultado de los examenes finales administrados en los turnos previstos se informara en todos los casos mediante un Acta de Evaluacion.


Documento: 5
Articulo: 121
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. TURNOS DE EXAMENES

Las actas de evaluacion deberan contener la siguiente informacion basica: a. Carrera. b. Asignatura y condicion (regular, libre o vocacional). c. Nomina de alumnos evaluados, calificacion final (en numeros y letras) obtenida por cada uno de ellos. d. Fecha de evaluacion. e. Total de alumnos inscriptos, examinados, ausentes, aprobados y no aprobados. f. Firma de los profesores del Tribunal Examinador.


Documento: 5
Articulo: 122
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. AUSENCIA A UN EXAMEN FINAL

a) Los alumnos que decidieren no presentarse a examen final habiendose inscripto para hacerlo deberan comunicar tal circunstancia en Departamento Alumnado por lo menos veinticuatro horas habiles antes de la constitucion del tribunal examinador, excepto casos de fuerza mayor, segun lo indicado en el Inc. d) del presente articulo. b) El desistimiento podra ser formalizado personalmente por el interesado o a traves de otra persona, en cuyo caso esta debera presentar su identificacion y el talon de inscripcion. c) Los alumnos que habiendose inscripto para rendir no se presentaren al examen final sin haber  dado cumplimiento a lo dispuesto en el inciso  anterior, no podran inscribirse para rendir examen final de la misma materia en el  llamado inmediato posterior. d) Los alumnos que habiendose inscripto para rendir una materia no hubieran desistido en el plazo estipulado, podran justificar la ausencia por razones de fuerza mayor, comunicando tal situacion mediante nota dirigida al responsable de la Unidad Academica , acompanada de la documentacion probatoria del impedimento. Esto debera hacerse efectivo dentro de las cuarenta y ocho horas habiles a partir del dia en que se haya constituido el tribunal examinador. e) Las causas del impedimento seran evaluadas por el responsable de la Unidad Academica quien decidira si otorga o no la justificacion  solicitada.




Documento: 5
Articulo: 123
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. MESAS EPECIALES

Queda autorizada la formacion de mesas especiales para administrar examen final en cualquier epoca del ano; dentro del periodo lectivo y fuera de los turnos previstos en el Calendario Academico  a los alumnos que adeuden como maximo 3 (tres) asignaturas para finalizar la carrera. Debera mediar al menos quince (15) dias entre el turno previsto en el Calendario Academico y la fecha de la mesa especial.


Documento: 5
Articulo: 124
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. MESAS EPECIALES

Los alumnos que se encuentren en tales condiciones deberan dirigirse por nota, cada vez, a la Secretaria Academica, solicitando una mesa especial de la asignatura cuyo final deseen rendir.


Documento: 5
Articulo: 125
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. MESAS EPECIALES

Secretaria Academica dispondra la constitucion del tribunal examinador y el dia y hora en que se integrara.


Documento: 5
Articulo: 126
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. MESAS EPECIALES

El Decano aprobara la conformacion de la mesa especial a propuesta de Secretaria Academica mediante resolucion.


Documento: 5
Articulo: 127
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. MESAS EPECIALES

El tribunal designado debera constituirse en la oportunidad prefijada y cumplimentar la correspondiente Acta de Evaluacion.




Documento: 5
Articulo: 128
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. MESAS EPECIALES

Los alumnos que habiendo solicitado mesa especial no se presentaren al examen sin haber dado a la vez cumplimiento a lo establecido en el Art. 28 Inc. a), b) y d) perderan el derecho a solicitar en lo sucesivo mesa especial de cualquier asignatura, por el termino de 6 (seis) meses sin perjuicio de lo establecido en el Art. 28 Inc. c).


Documento: 5
Articulo: 129
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. CALIFICACIONES

La calificacion final de cada asignatura se expresara en todos los casos en forma cuantitativa y cualitativa con la siguiente escala, no admitiendose decimales: 0 a 5 - (No aprobado). 6 - (Aprobado). 7 - (Bueno). 8 - (Muy bueno). 9-  (Distinguido). 10- (Sobresaliente).


Documento: 5
Articulo: 130
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. CALIFICACIONES

Se aplicara la correlacion de calificaciones entre la anterior y la nueva escala, transformando las notas consignadas con anterioridad a los alumnos y egresados, a traves de la siguiente tabla de conversion: Escala Anterior Equivalencia Nueva Escala 0 0 1 2 2 3 3 4,8 4 6 5 7 6 7,8 7 8,5 8 9 9 9,5 10 10


Documento: 5
Articulo: 131
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. CORRELATIVIDADES

A- Para inscribirse en las asignaturas que posean correlatividades anteriores se debera acreditar el cursado o la aprobacion de las instancias evaluatorias de las respectivas correlativas, de acuerdo a lo establecido en los regimenes de cada plan de estudio. B- Para la aprobacion definitiva de una asignatura que posea correlativas anteriores, cualquiera haya sido la modalidad de cursado, es requisito que el alumno apruebe las asignaturas correlativas previas.


Documento: 5
Articulo: 132
Capitulo: V. DE LOS TURNOS DE EXAMENES Y MESAS ESPECIALES. EXCEPCIONES A LAS CORRELATIVIDADES

Cuando se produzca un cambio de plan de estudio o surjan otras circunstancias extraordinarias que lo justifiquen, el Decano a sugerencia de Secretaria Academica podra autorizara solicitud de los alumnos interesados, excepciones transitorias a las normas del plan de correlatividades para cursar materias a los efectos de evitar una prolongacion imprevista de sus carreras.


Documento: 5
Articulo: 133
Capitulo: VI. DE LAS EQUIVALENCIAS

Los alumnos que hubieran aprobado en otras facultades o institutos de nivel superior asignaturas comprendidas en el Plan de estudios correspondientes a las carreras que esta cursando en la Facultad de Ciencia y Tecnologia de la Universidad Autonoma de Entre Rios, podran solicitar equivalencias de las mismas.


Documento: 5
Articulo: 134
Capitulo: VI. DE LAS EQUIVALENCIAS

La gestion se iniciara con una nota (modelo A)  Anexo I dirigida al Decano de la Facultad y en la que el interesado, debera especificar la o las asignaturas objeto del tramite.


Documento: 5
Articulo: 135
Capitulo: VI. DE LAS EQUIVALENCIAS

Conjuntamente con la nota, el solicitante debera presentar: a) Certificado expedido por la facultad o instituto de origen, en el que conste la nomina de las asignaturas aprobadas, calificaciones obtenidas y fechas de aprobacion. b) Copia autenticada de los programas analiticos con que el alumno cursara y aprobara la/s asignatura/s. c) En caso de que el programa analitico no incluyera la carga horaria correspondiente a la asignatura, debera presentar un informe sobre la misma, expedido por la autoridad del Establecimiento de origen.


Documento: 5
Articulo: 136
Capitulo: VI. DE LAS EQUIVALENCIAS

La documentacion sera remitida al profesor titular o responsable de la asignatura por la que se solicite equivalencia  en cada caso  quien emitira dictamen fundado, indicando si recomienda se otorgue equivalencia total, parcial o que no se otorgue. En el caso de equivalencia parcial, el docente debera indicar instancias de evaluacion complementarias y los temas correspondientes.


Documento: 5
Articulo: 137
Capitulo: VI. DE LAS EQUIVALENCIAS

La equivalencia para una asignatura puede otorgarse considerando mas de una materia aprobada en el establecimiento de origen.


Documento: 5
Articulo: 138
Capitulo: VI. DE LAS EQUIVALENCIAS

Para emitir su dictamen, el Profesor considerara los contenidos de la/s asignatura/s aprobada/s por el alumno en el Establecimiento de origen, de la carga horaria y todo aspecto cientifico, tecnico o didactico que estime pertinente. A tal efecto el docente debera completar la nota que se detalle en el Anexo I  (modelo B) elaborado por Departamento Alumnado.


Documento: 5
Articulo: 139
Capitulo: VI. DE LAS EQUIVALENCIAS

Las actuaciones seran elevadas a Secretaria Academica de la Facultad de Ciencia y Tecnologia, que las remitira al Decano para su tratamiento, pudiendo mantener la recomendacion del docente o apartarse de la misma con la debida fundamentacion. El Decano debera indicar en una Resolucion la nota obtenida  si se trata de equivalencia total  o las instancias de evaluacion.


Documento: 5
Articulo: 140
Capitulo: VI. DE LAS EQUIVALENCIAS

En el caso de ser reconocida una equivalencia total, lo que implica que el alumno es promovido en dicha asignatura, se tomara como valida la calificacion obtenida en la Unidad Academica de origen, o el promedio de las calificaciones obtenidas si en dicha equivalencia interviene mas de una asignatura.


Documento: 5
Articulo: 141
Capitulo: VI. DE LAS EQUIVALENCIAS

En el caso de equivalencia parcial, el alumno debera para ser promovido, aprobar las instancias de evaluacion que el Decano determine en el termino de un ano a partir de la fecha de Resolucion de otorgamiento de equivalencia. Las instancias de evaluacion fijadas en este caso, podran ser administradas hasta en 2 (dos) oportunidades en el transcurso del periodo de validez de la misma. Si vencido dicho plazo no hubiese cumplimentado los requisitos de la equivalencia, el mismo podra iniciar nuevamente el tramite correspondiente.


Documento: 5
Articulo: 142
Capitulo: VI. DE LAS EQUIVALENCIAS

El Departamento Alumnado labrara un acta correspondiente a las instancias de evaluacion realizadas que llevara la firma de quienes intervinieron en las mismas. La calificacion final correspondiente a esta asignatura sera el resultado del promedio entre la nota obtenida en el establecimiento original y la obtenida en las instancias de evaluacion fijadas.


Documento: 5
Articulo: 143
Capitulo: VII. TITULOS, DIPLOMAS Y CERTIFICADOS  

El personal del Departamento Alumnado tendra a su cargo la confeccion y entrega, a solicitud del alumno en cualquier estado de la carrera, de un certificado de las materias aprobadas para ser presentado ante quien lo requiera.


Documento: 5
Articulo: 144
Capitulo: VII. TITULOS, DIPLOMAS Y CERTIFICADOS

La Facultad otorgara a pedido de los alumnos que aprueben la totalidad de las materias de un plan de estudio de una determinada carrera, el Certificado analitico correspondiente, en el que conste su desempeno academico durante el desarrollo de la misma.


Documento: 5
Articulo: 145
Capitulo: VII. TITULOS, DIPLOMAS Y CERTIFICADOS

La Facultad otorgara a pedido de los alumnos que hayan aprobado la totalidad de las asignaturas del plan de estudio de una carrera, un diploma en el que conste el titulo profesional establecido en el respectivo plan. El diploma tendra un diseno uniforme confeccionado por Rectorado segun las normativas vigentes y sera firmado por el Rector, el Secretario Academico, el Decano y el Secretario Academico de la Facultad.


Documento: 5
Articulo: 146
Capitulo: VII. TITULOS, DIPLOMAS Y CERTIFICADOS. PROCEDIMIENTO PARA OTORGAR TITULOS Y DIPLOMAS

El Area Titulos tiene a su cargo la ejecucion de los procedimientos administrativos necesarios para la obtencion de titulos y diplomas segun la normativa vigente. El tramite debe ser iniciado por el alumno en el Area Titulos de la Sede/Subsede de la Facultad de donde egresa, presentando la siguiente documentacion pertinente; a tal efecto el Area Titulos confeccionara el expediente, verificara y corroborara la documentacion y los registros institucionales que avalen el efectivo cumplimiento por parte de los estudiantes de los requisitos de actuacion academica, reglamentarios y formales exigibles para acceder a los titulos y diplomas que la Universidad otorga.


Documento: 5
Articulo: 147
Capitulo: VII. TITULOS, DIPLOMAS Y CERTIFICADOS. PROCEDIMIENTO PARA OTORGAR TITULOS Y DIPLOMAS

En caso de perdida, sustraccion o destruccion total o parcial del original el graduado podra solicitar un duplicado del Titulo en la unidad academica de la cual egreso. El graduado o un tercero autorizado por este con poder especial certificado ante escribano, debera presentar una nota, y adjuntara las siguientes constancias: a) En caso de perdida o sustraccion: copia de la denuncia policial, la que se cotejara con el original. b) Si la destruccion es total: copia de la exposicion policial efectuada, la que se cotejara con el original. c) Si la destruccion es parcial: solo se procedera a la expedicion del duplicado si el deterioro afecta las partes escritas del Titulo.


Documento: 5
Articulo: 148
Capitulo: VIII. DE LOS DOCENTES

La Facultad contara con las siguientes categorias de Docentes Universitarios. a- Profesores titulares, Asociados, Adjuntos, Jefes de Trabajos Practicos y Auxiliares Docentes designados por concurso abierto de antecedentes y prueba de oposicion. b- Profesores Universitarios honorarios designados sin concurso ni prueba de oposicion. c- Docentes contratados o interinos y Auxiliares alumnos, mediante concursos abiertos segun Reglamentacion vigente, designados por la Facultad.


Documento: 5
Articulo: 149
Capitulo: VIII. DE LOS DOCENTES

Las funciones de los docentes Universitarios de la Facultad son las fijadas en el Titulo IV Seccion A Art. 49 a 67 del Estatuto Academico de la Universidad Autonoma de Entre Rios.


Documento: 5
Articulo: 150
Capitulo: VIII. DE LOS DOCENTES

Los Responsables de Carrera - cuya mision es la de coordinar y supervisar las actividades propias del desarrollo academico de las carreras a su cargo -, reuniran a los profesores de las respectivas catedras antes de la iniciacion del ano academico y por lo menos una vez durante su desarrollo, con el objeto de acordar criterios respecto del dictado de las mismas. Se labraran actas de estas reuniones las que seran informadas a Secretaria Academica.


Documento: 5
Articulo: 151
Capitulo: VIII. DE LOS DOCENTES

Normas para el dictado de clases. a- Las clases deben ser desarrolladas por el profesor a cargo del curso. Cuando otros docentes ajenos a la catedra dicten clases, el profesor a cargo del curso debera estar presente en el aula. b- Las clases practicas tambien podran estar a cargo de los profesores auxiliares y/o de los alumnos auxiliares. c- En caso de inasistencias, los profesores informaran con la debida antelacion, tomando los recaudos posibles para garantizar el normal desarrollo de las actividades aulicas.


Documento: 5
Articulo: 152
Capitulo: VIII. DE LOS DOCENTES. ORGANIZACION ACADEMICA

Los docentes de la sede y subsedes de la Facultad de Ciencia y Tecnologia elevaran, transcurridos los treinta dias de iniciado el desarrollo efectivo de las catedras los Programas y Planes de catedra y a los treinta dias de iniciado el primer cuatrimestre las Memorias de Catedra.


Documento: 5
Articulo: 153
Capitulo: VIII. DE LOS DOCENTES. ORGANIZACION ACADEMICA

Los formatos de presentacion de Programas, Planes y Memorias de Catedra deberan regirse por la normativa vigente en la Facultad o por las futuras modificaciones que pudieren producirse.


Documento: 5
Articulo: 154
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

Los docentes deberan asistir a los examenes finales de acuerdo a las fechas pautadas por el calendario academico fijado para cada ano academico. Deberan ademas constituir las mesas especiales que de acuerdo a los Art. 29 a 33 se sustancien.


Documento: 5
Articulo: 155
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

El Presidente de mesa asentara en el acta de examen correspondiente, inmediatamente despues de finalizado el acto de evaluacion, el resultado de las calificaciones del examen con la firma de los integrantes de la mesa, salvando con observacion y firma toda raspadura o enmienda.


Documento: 5
Articulo: 156
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

El resultado de cada examen, una vez calificado por la mesa de examen, es definitivo e inapelable.


Documento: 5
Articulo: 157
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

Los docentes examinadores son responsables de verificar la identidad de todos los examinados mediante la Libreta Universitaria o documentacion equivalente que se establezca y subsidiariamente con DNI, LE, LC o CI.


Documento: 5
Articulo: 158
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

Cualquiera de los profesores del tribunal debera firmar la constancia de asistencia al examen final a los alumnos que lo solicitaren. Estos certificados tendran valor una vez autenticados por el Departamento alumnado.


Documento: 5
Articulo: 159
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

Los docentes podran solicitar cambio, con la debida justificacion, en las fechas de examen por nota dirigida a Secretaria Academica, hasta dos dias posteriores a la notificacion de las mesas de examen. La misma sera resuelta por Secretaria Academica y debidamente notificada.


Documento: 5
Articulo: 160
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

El docente que revista en mas de un Establecimiento y al que excepcionalmente se le superpusieran tareas que le provocaran situacion transitoria y circunstancial de coincidencia horaria debera tener en cuenta el siguiente orden de prioridades: 1- Mesas examinadoras. 2- Dictados de clases. 3- Asistencia a reuniones de personal. 4- Actos y/o conferencias.


Documento: 5
Articulo: 161
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

No se justifican ausencias a mesas examinadoras por Razones Particulares. Por cada inasistencia no justificada a las mesas examinadoras, el profesor sufrira un descuento de su sueldo de acuerdo a la reglamentacion vigente. La inasistencia reiterada a las mesas examinadoras sera considerada falta grave, dando lugar a las sanciones reglamentarias pertinentes.


Documento: 5
Articulo: 162
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

En las fechas que se determinen por calendario academico los profesores de cada catedra completaran la condicion de cada alumno en una planilla provista por el Departamento alumnado, la que incluira: I. Carrera. II. Asignatura, curso y/o comision. III. Nomina de alumnos. IV. Detalle de la condicion de cada alumno: (Regular; Promocionado en forma directa, Libre o Vocacional). V. Fecha  de entrega y firma del profesor.


Documento: 5
Articulo: 163
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

El docente debera tener en cuenta para determinar la condicion de los alumnos lo siguiente: - Regular: Aquel alumno que satisface los requisitos exigidos por la catedra para acreditar tal condicion y que debe rendir examen final para aprobar la asignatura. - Promocionado en forma directa: Aquel alumno que haya aprobado las condiciones exigidas al efecto por la catedra y cumplimentado el Regimen de correlatividades correspondientes. - Libre: Aquel alumno que no alcanzo la condicion de regular en el transcurso del periodo lectivo o que se inscribiere como tal. - Vocacional: Aquel alumno que se inscriba para cursar una o varias asignaturas en carreras de la Facultad sin inscribirse a una determinada carrera sera considerado alumno vocacional.


Documento: 5
Articulo: 164
Capitulo: VIII. DE LOS DOCENTES. MESAS EVALUADORAS

El incumplimiento por parte de los alumnos y docentes de la Facultad de Ciencia y Tecnologia, de lo establecido en el presente Reglamento sera sancionado de acuerdo a lo que en cada caso establezca el Consejo Directivo de la Facultad, en concordancia con las normativas establecidas por el Consejo Superior de la Universidad.


Documento: 10
Articulo: 165
Capitulo: OBJETIVOS

1.1 Brindar a los alumnos la oportunidad de iniciar la carrera docente, o de actualizar y aplicar conocimientos. 1.2 Brindar a los alumnos la posibilidad de volcar los conocimientos adquiridos en el transcurso de su carrera, a traves de su insercion en las practicas de laboratorio o participando en proyectos especificos de informatizacion. 1.3 Enriquecer el proceso de ensenanza aprendizaje con el aporte de alumnos en caracter academico, bajo la supervision del responsable de catedra, del jefe de Laboratorio o del Responsable del Proyecto.


Documento: 10
Articulo: 166
Capitulo: FUNCIONES

2.1 En las catedras: Asistir a los alumnos en la realizacion de los trabajos practicos y colaborar y proponer la confeccion de guias teoricas y practicas. 2.2 En los laboratorios: a. Asistir al Jefe de Laboratorio Informatico tanto en la atencion de equipamiento existente en la Facultad, realizando tareas de instalacion de software, conexion y reparacion de hardware como en actividades de estudio y de investigacion relacionadas con temas especificos de dicho Laboratorio. b. Colaborar en la atencion de los distintos recursos existentes en los laboratorios de las carreras de la facultad y participar en actividades de estudio y de investigacion relacionadas con temas propios del Laboratorio correspondiente. 2.3. En los proyectos de informatizacion: Colaborar en el desarrollo de proyectos de informatizacion bajo la supervision del Responsable del Proyecto.


Documento: 10
Articulo: 167
Capitulo: REQUISITOS DE INSCRIPCION

3.1 Para inscribirse como aspirante a Alumno Auxiliar de catedra, el interesado debera acreditar: 3.1.1 Ser alumno regular de la carrera. 3.1.2 Haber aprobado la materia para la cual se inscribe. 3.1.3 Haber aprobado como minimo dos materias en los 12 (doce) meses anteriores al llamado a concurso. 3.2 Para inscribirse como aspirante a Alumno Auxiliar de laboratorio, el interesado debera acreditar: 3.2.1 Ser alumno regular de la carrera. 3.2.2 Haber aprobado el 50 % de las materias del departamento al que pertenezca el laboratorio, correspondientes al primer ciclo de la carrera, o acreditar idoneidad suficiente. 3.3 Para inscribirse como Auxiliar en el desarrollo de proyectos informaticos debera acreditar: 3.3.1. Ser alumno regular de la carrera. 3.3.2. Tener regularizadas las asignaturas de 2do ano. 3.3.3. Tener aprobadas las asignaturas que se fijen de acuerdo al proyecto.


Documento: 10
Articulo: 168
Capitulo: SELECCION DE POSTULANTES

4.1 Para la seleccion de Alumnos Auxiliares para una catedra o en laboratorios: Anualmente se habilitara, en funcion de las solicitudes de los Jefes de Departamento o del Responsable de Laboratorio y por el termino de cinco dias habiles un registro de aspirantes que los interesados se inscribiran mediante nota a la que acompanaran los antecedentes que acrediten. 4.2 Para la seleccion de Alumnos Auxiliares para los proyectos de informatizacion: La convocatoria se hara ante la necesidad concreta, de implementar una tarea especifica de informatizacion en algun area de la facultad. 4.3. Cerrado el registro, el jurado que se designe en los terminos del punto 5, evaluara la documentacion presentada y confeccionara el orden de meritos correspondiente. Con el llamado a inscripcion se estableceran las pautas a tener en cuenta para la evaluacion de los aspirantes, segun lo estipule cada catedra con conformidad del respectivo Jefe de Departamento o del Responsable de Laboratorio si correspondiere. 4.4 En todos los casos si el aspirante se ha desempenado con anterioridad como Auxiliar Alumno, se considerara para su evaluacion el informe presentado por el responsable de catedra, el Jefe de Departamento o Responsable Informatico, segun lo previsto en el articulo 8.


Documento: 10
Articulo: 169
Capitulo: JURADO

- El jurado para la seleccion de Alumno Auxiliar de Catedra estara constituido por: El Jefe de Departamento que corresponda, coordinador de catedra si existiera, profesor de la materia y un alumno designado por el Decano Organizador a propuesta de los Consejeros alumnos del Consejo Consultivo. Si en dicha materia no cuenta con Coordinador de Catedra, se designara un docente de la catedra o de catedra afin. - El jurado para la seleccion del Alumno Auxiliar de Laboratorio esta constituido por: Jefe del Departamento que corresponda, Jefe del Laboratorio y un alumno designado por el Decano Organizador a propuesta de los Consejeros alumnos del Consejo Consultivo. - El jurado para la seleccion del Alumno Auxiliar de Proyectos Informaticos estara constituido por: El Jefe del departamento correspondiente de acuerdo al proyecto, el Responsable del proyecto de Informatizacion y alumno designado por el Decano Organizador a propuesta de los Consejeros alumnos del Consejo Consultivo. 5.1 El jurado alumno debera rendir las siguientes condiciones: 5.1.1 Ser alumno regular de la Facultad. 5.1.2 Haber aprobado la materia que se concursa. 5.1.3 Cumplir el punto 3.2.2 o el punto 3.3.2 segun corresponda.


Documento: 10
Articulo: 170
Capitulo: EVALUACION DE ANTECEDENTES

El jurado en forma conjunta debera evaluar los antecedentes teniendo en cuenta: 6.1 Desempeno academico (nota en la asignatura, promedio en la carrera, materias aprobadas, regularizadas, rendimiento academico). 6.2 Ayudantias, cursos, becas, idiomas y otros antecedentes.


Documento: 10
Articulo: 171
Capitulo: DESIGNACION

7.1 Las designaciones seran efectuadas por el Decano Organizador de la Facultad de acuerdo con el orden de meritos. 7.2 Cada alumno podra ser designado en una sola asignatura, Laboratorio o Proyecto. 7.3 Las designaciones tendran vigencia durante el ano academico al que corresponda y, en caso de Proyectos, por el tiempo previsto para la culminacion de los mismos. Sin perjuicio de ello caducaran: 7.3.1 Por renuncia del interesado. 7.3.2 Por egreso del interesado. 7.3.3 Por resolucion del Decano Organizador y a solicitud debidamente fundamentada, por el profesor de la catedra, del Jefe de Laboratorio o del Responsable de Proyecto de Informatizacion, previo conocimiento del Jefe de Departamento correspondiente. 7.4 Las designaciones pueden ser prorrogadas sin necesidad de un nuevo concurso, por unica vez, cuando el Alumno Auxiliar cuente con un informe del Responsable de Catedra, Jefes del Laboratorio o del Responsable de Proyecto, sobre su desempeno, y haya aprobado por lo menos dos materias durante el ano anterior.


Documento: 10
Articulo: 172
Capitulo: EVALUACION

8.1 Al finalizar el ano lectivo, el Profesor Responsable de la Catedra debera presentar al Coordinador de la misma, al Jefe de Departamento y este a la Secretaria Academica un informe sobre el desempeno del Alumno Auxiliar, indicando ademas las tareas realizadas el ayudante alumno, indicando ademas las tareas realizadas. 8.2 Al finalizar el ano lectivo el alumno Auxiliar debera presentar al Profesor Responsable, al Coordinador de la catedra o al Jefe de Laboratorio, al Jefe de Departamento y este a la Secretaria Academica un informe sobre su desempeno, indicando ademas las tareas realizadas durante ese periodo. 8.3 Cuando se trate de Proyectos de Informatizacion el informe debera ser presentado al finalizar el mismo.


Documento: 11
Articulo: 173
Capitulo: DE LOS DIRECTORES DE CARRERA

Cada carrera de la Facultad de Ciencia y Tecnologia, dependiente de la Universidad Autonoma de Entre Rios contara con un Director de Carrera titular y uno suplente, cuyas funciones y modalidad de eleccion estaran estipuladas por el presente Reglamento.


Documento: 11
Articulo: 174
Capitulo: DE LOS DIRECTORES DE CARRERA

A los efectos de este reglamento se entendera por "carrera" a todas aquellas titulaciones de un mismo campo de conocimiento y/o actividad; razon por la cual, en este caso, una carrera involucra a las titulaciones de tecnicatura, profesorado y licenciatura.


Documento: 11
Articulo: 175
Capitulo: DE LOS DIRECTORES DE CARRERA

Para aquellas carreras que se dicten simultaneamente en varias sedes de la Facultad, se elegira un Director titular y uno suplente para cada una de ellas.


Documento: 11
Articulo: 176
Capitulo: DE LOS DIRECTORES DE CARRERA

Academicamente, el Director dependera de la Secretaria Academica, debiendo dar cuenta a esta de sus actividades, o ante quienes esta Secretaria delegue la funcion.


Documento: 11
Articulo: 177
Capitulo: DE LOS DIRECTORES DE CARRERA

Para ser electo Director de Carrera se requiere poseer titulo afin a la carrera para la que se postula, ser profesor de materias especificas a la orientacion de la carrera, en la categoria de profesor titular, asociado o adjunto de la misma y poseer una antiguedad minima de 3 (tres) anos en ejercicio de la docencia en la carrera.


Documento: 11
Articulo: 178
Capitulo: DE LOS DIRECTORES DE CARRERA

Los Directores de Carrera duraran 2 (dos) anos en sus funciones, pudiendo ser reelegidos solo por un nuevo periodo consecutivo.


Documento: 11
Articulo: 179
Capitulo: DE LOS DIRECTORES DE CARRERA

Quien resulte electo para desempenar la funcion de Director de Carrera en una de las carreras de la Facultad no podra ocupar identica responsabilidad en otra, aunque esta fuera en caracter de suplente.


Documento: 11
Articulo: 180
Capitulo: DE LOS DIRECTORES DE CARRERA

El Director de Carrera electo como titular recibira una compensacion economica por su funcion, la cual se remunerara en 10 (diez) horas catedras, equivalente a un cargo de profesor Asociado, Dedicacion Simple.


Documento: 11
Articulo: 181
Capitulo: DE LOS DIRECTORES DE CARRERA

El Director de Carrera debera cumplir al menos con el 60% de lo que implica una dedicacion Simple de Profesor Asociado, equivalente a 6 horas semanales, distribuidas en no menos de 3 (tres) dias a la semana, asegurando que no se superpongan con el horario de las actividades propias del desarrollo de la/s catedras a su cargo.


Documento: 11
Articulo: 182
Capitulo: DE LOS DIRECTORES DE CARRERA

La actividad del Director suplente es ad-honorem, a menos que se produzca licencia por mas de 30 (treinta) dias del titular o renuncia al cargo, computandose las licencias consecutivas. En estos ultimos casos, el Decano reasignara la compensacion economica al suplente, quien sera designado hasta completar el periodo de los 2 (dos) anos o hasta que el titular se reintegre en sus funciones, segun corresponda.


Documento: 11
Articulo: 183
Capitulo: DE LOS DIRECTORES DE CARRERA

Seran funciones del Responsable: a) Presidir los Consejos de Carrera. b) Participar en el diseno, rediseno y actualizacion del Plan de Estudios de la carrera. c) Colaborar en el proceso de evaluacion institucional. d) Informar y coordinar las solicitudes, designaciones y evaluaciones de los alumnos auxiliares y de tutores y de las actividades desarrolladas en las distintas catedras. e) Participar en la organizacion, puesta en marcha y evaluacion de las actividades propuestas para los Cursos Introductorios de su carrera. d) Participar en las instancias de concursos que la reglamentacion especifica indique. e) Colaborar con la Secretaria Academica y la Subsecretaria de Gestion Academica y con el Area Alumnado de la Facultad en la confeccion de los horarios de los profesores de la carrera. f) Observar y comunicar, a la Subsecretaria de Gestion Academica de la Facultad, la necesidad de cobertura de catedras a los efectos de lograr una adecuada implementacion de los planes de estudios correspondientes. g) Identificar las areas en que se requiera capacitacion para los profesores de la carrera. h) Promover, junto a la Secretaria Academica y a la Subsecretaria de Gestion Academica espacios de intercambio e integracion entre los Directores de otras carreras de la Facultad y de la misma carrera de distintas subsedes. i) Promover la realizacion de proyectos de investigacion y extension, de acuerdo con las lineas previstas por los respectivos Secretarios. j) Velar por el buen funcionamiento de los servicios auxiliares de la docencia, la investigacion y la extension vinculados con la carrera a su cargo (biblioteca, equipamiento informatico, etc.). k) Relevar y proponer la adquisicion de material bibliografico requerido por las catedras e informar de esta situacion a la Secretaria Academica de su dependencia y a traves de esta al Area Biblioteca. l) Propiciar la existencia de ofertas extracurriculares que aborden temas que complementen los incluidos en el plan de estudio de la carrera. m) Participar activamente, en representacion de la Facultad, en las Asociaciones, Federaciones, Redes o Instituciones que hacen al campo de la carrera. n) Convocar mensualmente (como minimo) a una reunion de Consejo de Carrera, labrando acta de lo actuado, esta debera ser firmada por todos los presentes. o) Elaborar un informe anual de actividades realizadas, el cual debera ser presentado ante la Secretaria Academica y, por intermedio de esta, al Decanato de la Facultad. En dicho informe, ademas, se debera dar cuenta de la planificacion proyectada para el ano siguiente, incluyendo un diagnostico de necesidades, prioridades y requerimientos presupuestarios; previa vista del Consejo de Carrera.


Documento: 11
Articulo: 184
Capitulo: DE LOS DIRECTORES DE CARRERA

El Director de Carrera sera elegido por sus pares en eleccion directa, por simple mayoria de sufragios, pudiendo ser elegido entre todos los docentes de la carrera, que cumplan lo dispuesto en el Articulo 5o del presente Reglamento.


Documento: 11
Articulo: 185
Capitulo: DE LOS DIRECTORES DE CARRERA

La eleccion de los Directores sera simultanea en todas las carreras de la Facultad, en tiempo a determinar, mediante la convocatoria del Decano.


Documento: 11
Articulo: 186
Capitulo: DE LOS DIRECTORES DE CARRERA

El Consejo Directivo fijara el cronograma electoral que debera incluir fechas para la presentacion de postulaciones, plazo para oficializacion de los postulantes, para impugnaciones y para la resolucion del comicio, fecha de proclamacion y asuncion de los electos, y designara a la Junta Electoral que tendra la responsabilidad para la Sede y para cada Subsede de fiscalizar el normal desarrollo de la eleccion, desde su inicio hasta su finalizacion.


Documento: 11
Articulo: 187
Capitulo: DE LOS DIRECTORES DE CARRERA

La Junta Electoral estara constituida por 3 (tres) docentes titulares y 3 (tres) suplentes de cualquier categoria, con una antiguedad en alguna catedra de la carrera minima de 1 (un) ano, designados por el Decano a propuesta de los representantes docentes del Consejo Directivo. Los docentes que integren la Junta Electoral no podran participar como elegibles en los cargos en disputa.


Documento: 11
Articulo: 188
Capitulo: DE LOS DIRECTORES DE CARRERA

El Departamento Personal de la Facultad confeccionara para cada carrera de cada sede y/o subsede: a) La lista de electores con su correspondiente antiguedad en la Facultad conforme con el Articulo 17 del presente reglamento. b) La lista de elegibles, conforme con el Articulo 5. La Junta Electoral exhibira la convocatoria y los mencionados padrones en los transparentes que la Facultad destine para ello y en la pagina web de la Facultad, con una antelacion de 10 dias habiles a la fecha fijada para el inicio del acto eleccionario. Cualquier reclamo debera realizarse por escrito una vez publicado los padrones y hasta 3 (tres) dias habiles anteriores al inicio del acto eleccionario. La Junta Electoral debera expedirse al respecto dentro de los 3 (tres) dias habiles posteriores a la presentacion del reclamo.


Documento: 11
Articulo: 189
Capitulo: DE LOS DIRECTORES DE CARRERA

La emision del voto sera secreta, obligatoria y directa.


Documento: 11
Articulo: 190
Capitulo: DE LOS DIRECTORES DE CARRERA

Seran electores aquellos docentes de la carrera a la cual pertenece su catedra, laboratorio y/o proyecto de investigacion y desarrollo, cualquiera sea su categoria y caracter de designacion que tengan como minimo 1 (un) ano de antiguedad en la carrera y subsede correspondiente.


Documento: 11
Articulo: 191
Capitulo: DE LOS DIRECTORES DE CARRERA

Para ser oficializada una postulacion se debera presentar una nota dirigida a la Junta Electoral, manifestando las aspiraciones al cargo, el nombre del candidato titular y suplente y una nomina firmada por no menos del 15% del total de electores que avalen la candidatura.


Documento: 11
Articulo: 192
Capitulo: DE LOS DIRECTORES DE CARRERA

La presentacion a la que alude el articulo anterior debe realizarse 5 (cinco) dias habiles previos a la eleccion. Vencido el plazo de 48 horas de la presentacion y no habiendose expedido la Junta, se dara por oficializada la candidatura. Si dentro del plazo previsto mediare alguna observacion, el postulante sera informado de la misma a fin de que subsane el inconveniente, lo cual debera realizarse en el termino de las 24 horas siguientes.


Documento: 11
Articulo: 193
Capitulo: DE LOS DIRECTORES DE CARRERA

La emision de votos se realizara durante 5 (cinco) dias habiles corridos en los horarios establecidos por la Junta Electoral para cada acto eleccionario. A tal fin se habilitara: a) Una urna por cada carrera en cada sede y designara 1 (un) RESPONSABLE del acto electoral por cada una. b) Una copia del padron de electores de cada carrera en cada sede para la firma del votante despues de haber emitido su voto.


Documento: 11
Articulo: 194
Capitulo: DE LOS DIRECTORES DE CARRERA

Para la emision del voto el sufragante debera presentar Documento de Identidad, Libreta Civica, de Enrolamiento o Cedula. Cuando no se pueda establecer inequivocamente la identidad del elector no se estara en condiciones de emitir el voto.


Documento: 11
Articulo: 195
Capitulo: DE LOS DIRECTORES DE CARRERA

Seran pasibles de sancion, aquellos electores que no voten sin justificacion fundada por escrito. A los efectos de dar una efectiva justificacion, debera ser dirigida a la Junta Electoral en el plazo de 30 (treinta) dias habiles a contar a partir del cierre del acto eleccionario.


Documento: 11
Articulo: 196
Capitulo: DE LOS DIRECTORES DE CARRERA

El escrutinio se realizara inmediatamente de concluido el acto eleccionario. Estara presidido por 1 (un) integrante de la Junta Electoral y 1 (un) representante del Decanato pudiendo estar presente como minimo 1 (un) representante de cada carrera, el cual debera ser integrante del padron electoral de la misma. Esta comision labrara un acta con el resultado del escrutinio definitivo y la nomina de los electores que no emitieron su voto junto con toda la documentacion pertinente que se haya generado. Dicha documentacion se elevara al Decano, para su tratamiento en el Consejo Directivo, en la primera reunion posterior al cierre del acto eleccionario. El plazo de impugnaciones y/o reclamos con relacion al acto eleccionario sera de 3 (tres) dias habiles posteriores al cierre del mismo.


Documento: 11
Articulo: 197
Capitulo: DE LOS DIRECTORES DE CARRERA

En caso de empate se realizara una segunda votacion la cual se desarrollara en 1 (un) solo dia dentro de los 5 (cinco) dias habiles siguientes con las mismas exigencias y procedimientos establecidos para la primera votacion.


Documento: 11
Articulo: 198
Capitulo: DE LOS DIRECTORES DE CARRERA

En caso de no presentarse ninguna postulacion al cargo, para las fechas previstas a elecciones de Director de Carrera, se debera convocar nuevamente en esa Sede y/o Carrera en un plazo no mayor a 30 dias.


Documento: 11
Articulo: 199
Capitulo: DE LOS DIRECTORES DE CARRERA

Las actuaciones, deliberaciones y resoluciones de la Junta Electoral deberan constar en Actas debidamente foliadas y firmadas por sus miembros. Esta documentacion, una vez finalizado el comicio, sera archivada por la Secretaria Academica.


Documento: 11
Articulo: 200
Capitulo: DE LOS DIRECTORES DE CARRERA

Cualquier aspecto no previsto en este Reglamento sera resuelto por el Decano, quien podra dar curso y decision a los miembros de la Junta Electoral.


Documento: 11
Articulo: 201
Capitulo: DE LOS CONSEJOS DE CARRERA

Los Consejos de Carrera son ambitos de discusion, reflexion y participacion, los cuales estaran integrados con voz y voto por representantes del Claustro docente, estudiantil y graduados, debiendo estos ser elegidos por sus estamentos, estaran conformados por 2 (dos) docentes, 2 (dos) alumnos y 1 (un) graduado, titular y suplente.


Documento: 11
Articulo: 202
Capitulo: DE LOS CONSEJOS DE CARRERA

Seran presididos por el Director  de Carrera quien tendra voz y voto, y en caso de empate su voto se computara doble.  


Documento: 11
Articulo: 203
Capitulo: DE LOS CONSEJOS DE CARRERA

Seran funciones de los Consejos de Carreras: a) Participar en la evaluacion del proceso de implementacion del plan de estudios de la carrera y proponer, cuando resulte necesario, la actualizacion del mismo. b) Propiciar espacios de reflexion entre docentes, estudiantes, graduados, personal administrativo y autoridades de la carrera a los efectos de elaborar propuestas inherentes a la adecuada implementacion del plan de estudio de la carrera respectiva. c) Sugerir criterios para la reubicacion de docentes o en su defecto para que se proceda a la convocatoria a concursos, segun la reglamentacion vigente. d) Atender los problemas que se originen en la reubicacion de docentes, como primera instancia de apelacion. d) Proponer normativa academica para la carrera. e) Proponer a las autoridades la realizacion de convenios con organizaciones publicas, privadas y de la sociedad civil, cuya vinculacion institucional resulte de interes para la carrera correspondiente. f) Proponer la adquisicion de insumos y otros recursos destinados a la ensenanza. g) Proponer acciones tendientes a fortalecer la insercion de la carrera en el medio social. h) Propiciar la existencia de ofertas extracurriculares que aborden temas que complementen los incluidos en el plan de estudios de la carrera. i) Proponer e incentivar lineas prioritarias en actividades de Extension e Investigacion.


Documento: 11
Articulo: 204
Capitulo: DE LOS CONSEJOS DE CARRERA

Los docentes, alumnos y egresados integrantes del consejo de carrera seran elegidos por sus pares de la carrera respectiva, en eleccion directa, por simple mayoria de sufragios. En caso de empate se realizara una nueva eleccion entre los postulantes que hubieran obtenido mayor numero de votos hasta obtener la mayoria necesaria.


Documento: 11
Articulo: 205
Capitulo: DE LOS CONSEJOS DE CARRERA

Las elecciones de representantes a Consejo de Carrera se realizaran conjuntamente con las de Director de Carrera y Jefes de Departamento.


Documento: 11
Articulo: 206
Capitulo: DE LOS CONSEJOS DE CARRERA

Para ser elector como representantes docentes en el Consejo de Carrera y para ser electos de los mismos se requiere cumplir las condiciones fijadas en el articulo 18o del presente.


Documento: 11
Articulo: 207
Capitulo: DE LOS CONSEJOS DE CARRERA

Para ser elector, el alumno debera tener al menos 3 asignaturas aprobadas al momento de la convocatoria a elecciones. Para ser elegible como representante alumno al Consejo de Carrera debera tener el 30% de la carrera aprobada.


Documento: 11
Articulo: 208
Capitulo: DE LOS CONSEJOS DE CARRERA

Los representantes del Consejo de carrera duraran 2 (dos) anos en sus funciones y desempenaran las mismas ad-honorem.


Documento: 12
Articulo: 209
Capitulo: 

Apruebese el Reglamento General de Practica Docente de la Facultad de Ciencia y Tecnologia de la Universidad Autonoma de Entre Rios en los terminos que se detallan en el ANEXO UNICO de la presente Resolucion.


Documento: 12
Articulo: 210
Capitulo: 

Deroguese cualquiera otra norma vigente a la fecha que se oponga a la presente.


Documento: 12
Articulo: 211
Capitulo: 

Establecese que el presente reglamento aprobado en el articulo precedente entrara en vigencia a partir del presente Ano Academico para las carreras de esta Facultad en cuyos planes de estudios se incluyan las catedras Practica Docente I y II.


Documento: 12
Articulo: 212
Capitulo: 

Registrese, comuniquese, notifiquese a las partes interesadas y cumplido, archivese.


Documento: 12
Articulo: 213
Capitulo: I - FINALIDAD

El presente marco regulatorio comun tiene como objeto establecer parametros, pautas y criterios generales en orden a la realizacion de las actividades inherentes al desarrollo de las practicas docentes establecidas en los respectivos planes de estudio. Ello asi, las distintas catedras de Practica Docente de las diversas carreras de formacion docente que se cursan en el ambito de esta Facultad deberan ajustar sus planificaciones de catedra a la presente normativa, sin que ello obste que en las mismas se contemple la naturaleza, las especificidades y las particularidades propias de cada disciplina cientifica y, consecuentemente, de cada carrera y del correspondiente perfil del egresado.


Documento: 12
Articulo: 214
Capitulo: II - LA FORMACION ACADEMICA Y LA FORMACION PROFESIONAL EN LA PRACTICA DOCENTE

a) La Practica Docente, como proceso formativo, si bien se vincula a la formacion academica en sentido lato, pertenece a la formacion profesional en sentido estricto (esto es, a las competencias necesarias para el ejercicio especifico de la profesion docente). Por ello, la formacion academica previa es condicion de posibilidad de la practica y en consecuencia se asume como un pre-requisito excluyente para el acceso y permanencia en la misma por parte de los alumnos. b) En la planificaciones de las catedras de Practica Docente, los titulares de las mismas, estableceran taxativamente los extremos que supondran la eviccion inmediata e irreversible de los alumnos  en cualquier fase de la practica - cuyo desempeno evidencie deficiencias inherentes a la formacion academica; lo cual incluye el problema de la competencia institucional de los contenidos de la ciencia (esto es, lo que se debe y puede ensenar en la escuela y su metodologia inherente), ademas de lo senalado en el punto precedente.


Documento: 12
Articulo: 215
Capitulo: III - CONFORMACION DE LOS EQUIPOS DE CATEDRAS DE PRACTICA DOCENTE

Los equipos de catedra a cargo de las practicas docentes se conformaran del siguiente modo: a) Profesores responsables. b) Profesores auxiliares por cada grupo de doce (12) alumnos o fraccion. En todos los casos, los docentes a cargo de la Practica Docente deberan acreditar competencias cientificas especificas y competencias metodologicas en las disciplinas objeto de las practicas.


Documento: 12
Articulo: 216
Capitulo: IV - CRITERIOS PARA LA SELECCION DE LA INSTITUCIONES EDUCATIVAS DONDE SE LLEVARAN A CABO LAS PRACTICAS DOCENTES

Las instituciones educativas deberan ser seleccionadas, en la medida de las posibilidades facticas que permitan las condiciones del medio, atendiendo basicamente a los siguientes criterios: a) Instituciones educativas con poblacion estudiantil proveniente de distintos sectores sociales, economicos y culturales. b) Ubicacion geografica diversificada (instituciones centricas, perifericas y suburbanas). c) Diversidad de caracteristicas institucionales, de culturas institucionales, de estilos de conduccion y de proyectos educativos institucionales.


Documento: 12
Articulo: 217
Capitulo: VI - ORGANIZACION DE LAS PRACTICAS DOCENTES

Las practicas docentes incluiran las siguientes fases, tanto para el 3er. como para el 4to. ano de las carreras: Fase 1: Practicas de observacion. Fase 2: Practicas preliminares. Fase 3: Residencia. En todos los casos, la extension, el nivel del sistema educativo y la diversidad de asignaturas en que se realicen las practicas seran determinadas por los docentes a cargo de las catedras de Practica Docente en funcion del rendimiento de los alumnos, del perfil del egresado y de los alcances del titulo establecidos para cada carrera, ademas de los topicos consignados en el Punto IV. En cuanto a la duracion de cada una de las fases, las mismas seran determinadas por los responsables de las respectivas catedras de Practica Docente. A tal efecto se establecera la extension minima y maxima de cada fase. Se propendera a la utilizacion de criterios preminentemente cualitativos. La practica docente no podra extenderse mas alla del 30 de octubre del respectivo ano lectivo.


Documento: 12
Articulo: 218
Capitulo: VII - REGISTROS

Cada catedra de Practica Docente debera elaborar, y anexar, a la respectiva planificacion de catedra las siguientes documentales, sin perjuicio de otras que se consideren pertinentes:  Modelo de registro de observaciones.  Modelos de diagnostico aulico y del contexto institucional.  Modelos de planificaciones.  Modelos de criticas pedagogicas.  Modelo de informe auto-evaluativo final del alumno.  Modelo de informe del equipo de Practica Docente a Secretaria Academica.  Modelo de registro de seguimiento evaluativo sistematico de las distintas actividades llevadas a cabo por los alumnos en las instituciones educativas donde realicen las practicas.


Documento: 12
Articulo: 219
Capitulo: VIII - TRAMITACIONES ANTE LAS INSTITUCIONES EDUCATIVAS DONDE SE LLEVARAN A CABO LAS PRACTICAS DOCENTES

Los docentes responsables de las catedras de Practica Docente tendran a su cargo los aspectos organizativos y burocraticos inherentes a las practicas de los alumnos en las diversas instituciones educativas seleccionadas. Esto implicara: a) Solicitud formal de autorizacion para la realizacion de las practicas, tramitada por ante las autoridades de la institucion donde se llevaran a cabo las mismas, con descripcion prospectiva sistematica de los circunstanciales de tiempo y modo de las actividades aulicas y extra-aulicas previstas. Dicha solicitud debera rubricarse conjuntamente con la Secretaria Academica o con el Decanato de la Facultad de Ciencia y Tecnologia. b) Los profesores responsables de las catedras de Practica Docente elevaran periodicamente por ante la Secretaria Academica un informe sintetico del desarrollo de las practicas en las instituciones seleccionadas y de cualquier otra condicion o circunstancia que se considere relevante poner en conocimiento de las autoridades academicas de la Facultad.


Documento: 12
Articulo: 220
Capitulo: IX - FIRMA DE CONVENIOS CON LAS INSTITUCIONES EDUCATIVAS EN LAS QUE  SE REALICEN LAS PRACTICAS DOCENTES

Los docentes responsables de las catedras de Practica Docente podran proponer formalmente al Decanato de la Facultad de Ciencia y Tecnologia la celebracion de convenios de cooperacion inter-institucional con las instituciones educativas donde se lleven a cabo las practicas objeto de esta Resolucion. Dichos convenios seran formalizados por las autoridades academicas de la Facultad de Ciencia y Tecnologia de la Universidad Autonoma de Entre Rios. Mediante los mismos (y con la signatura de los correspondientes Protocolos Facultativos o Adicionales) podran establecerse mecanismos de asistencia academica por parte de los alumnos practicantes a alumnos con dificultades de aprendizaje de los cursos en los que se verifican las practicas. Dicha asistencia consistira en clases o instancias sistematicas de consulta, apoyo, tutoria o reemplazo del titular de la catedra por ausencia temporaria del mismo. En todos los casos, los alumnos practicantes que desarrollen dichas actividades, acumularan creditos academicos a los efectos de la aprobacion de la Practica Docente.


Documento: 13
Articulo: 221
Capitulo: TITULO I: DISPOSICIONES PRELIMINARES

Estan comprendidas dentro de la presente ley las universidades e institutos universitarios, estatales o privados autorizados y los institutos de educacion superior de jurisdiccion nacional, provincial o de la Ciudad Autonoma de Buenos Aires, de gestion estatal o privada, todos los cuales forman parte del Sistema Educativo Nacional, regulado por la ley 26.206 Ley de Educacion Nacional. El Estado nacional, las provincias y la Ciudad Autonoma de Buenos Aires, tienen la responsabilidad principal e indelegable sobre la educacion superior, en tanto la educacion y el conocimiento son un bien publico y un derecho humano personal y social en el marco de lo establecido por la ley 26.206.(Articulo sustituido por art. 1 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 222
Capitulo: TITULO I: DISPOSICIONES PRELIMINARES

El Estado nacional es el responsable de proveer el financiamiento, la supervision y fiscalizacion de las universidades nacionales, asi como la supervision y fiscalizacion de las universidades privadas. Las provincias y la Ciudad Autonoma de Buenos Aires son los responsables de proveer el financiamiento, la supervision y fiscalizacion de los institutos de formacion superior de gestion estatal y de las universidades provinciales, si las tuviere, de su respectiva jurisdiccion. Las provincias y la Ciudad Autonoma de Buenos Aires son los responsables de la supervision, la fiscalizacion y, en los casos que correspondiere, la subvencion de los institutos de formacion superior de gestion privada en el ambito de su respectiva jurisdiccion. La responsabilidad principal e indelegable del Estado nacional, las provincias y la Ciudad Autonoma de Buenos Aires, sobre la educacion superior, implica: a) Garantizar la igualdad de oportunidades y condiciones en el acceso, la permanencia, la graduacion y el egreso en las distintas alternativas y trayectorias educativas del nivel para todos quienes lo requieran y reunan las condiciones legales establecidas en esta ley; b) Proveer equitativamente, en la educacion superior de gestion estatal, becas, condiciones adecuadas de infraestructura y recursos tecnologicos apropiados para todas aquellas personas que sufran carencias economicas verificables; c) Promover politicas de inclusion educativa que reconozcan igualitariamente las diferentes identidades de genero y de los procesos multiculturales e interculturales; d) Establecer las medidas necesarias para equiparar las oportunidades y posibilidades de las personas con discapacidades permanentes o temporarias; e) Constituir mecanismos y procesos concretos de articulacion entre los componentes humanos, materiales, curriculares y divulgativos del nivel y con el resto del sistema educativo nacional, asi como la efectiva integracion internacional con otros sistemas educativos, en particular con los del Mercosur y America Latina; f) Promover formas de organizacion y procesos democraticos; g) Vincular practicas y saberes provenientes de distintos ambitos sociales que potencien la construccion y apropiacion del conocimiento en la resolucion de problemas asociados a las necesidades de la poblacion, como una condicion constitutiva de los alcances instituidos en la ley 26.206 de educacion nacional (titulo VI, La calidad de la educacion, capitulo I, "Disposiciones generales", articulo 84). (Articulo sustituido por art. 2 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 223
Capitulo: TITULO I: DISPOSICIONES PRELIMINARES

Los estudios de grado en las instituciones de educacion superior de gestion estatal son gratuitos e implican la prohibicion de establecer sobre ellos cualquier tipo de gravamen, tasa, impuesto, arancel, o tarifa directos o indirectos. Prohibase a las instituciones de la educacion superior de gestion estatal suscribir acuerdos o convenios con otros Estados, instituciones u organismos nacionales e internacionales publicos o privados, que impliquen ofertar educacion como un servicio lucrativo o que alienten formas de mercantilizacion. (Articulo incorporado por art. 3 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 224
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 1: De los fines y objetivos



La Educacion Superior tiene por finalidad proporcionar formacion cientifica, profesional, humanistica y tecnica en el mas alto nivel, contribuir a la preservacion de la cultura nacional, promover la generacion y desarrollo del conocimiento en todas sus formas, y desarrollar las actitudes y valores que requiere la formacion de personas responsables, con conciencia etica y solidaria, reflexivas, criticas, capaces de mejorar la calidad de vida, consolidar el respeto al medio ambiente, a las instituciones de la Republica y a la vigencia del orden democratico.


Documento: 13
Articulo: 225
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 1: De los fines y objetivos

Son objetivos de la Educacion Superior, ademas de los que establece la ley 24.195 en sus articulos 5o, 6o, 19o y 22o: a) Formar cientificos, profesionales y tecnicos, que se caractericen por la solidez de su formacion y por su compromiso con la sociedad de la que forman parte; b) Preparar para el ejercicio de la docencia en todos los niveles y modalidades del sistema educativo; c) Promover el desarrollo de la investigacion y las creaciones artisticas, contribuyendo al desarrollo cientifico, tecnologico y cultural de la Nacion; d) Garantizar crecientes niveles de calidad y excelencia en todas las opciones institucionales del sistema; e) Profundizar los procesos de democratizacion en la Educacion Superior, contribuir a la distribucion equitativa del conocimiento y asegurar la igualdad de oportunidades; f) Articular la oferta educativa de los diferentes tipos de instituciones que la integran; g) Promover una adecuada diversificacion de los estudios de nivel superior, que atienda tanto las expectativas y demandas de la poblacion como a los requerimientos del sistema cultural y de la estructura productiva; h) Propender a un aprovechamiento integral de los recursos humanos y materiales asignados; i) Incrementar y diversificar las oportunidades de actualizacion, perfeccionamiento y reconversion para los integrantes del sistema y para sus egresados; j) Promover mecanismos asociativos para la resolucion de los problemas nacionales, regionales, continentales y mundiales.


Documento: 13
Articulo: 226
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 2: De la estructura y articulacion

La Educacion Superior esta constituida por institutos de educacion superior, sean de formacion docente, humanistica, social, tecnico-profesional o artistica. y por instituciones de educacion universitaria, que comprende universidades e institutos universitarios. (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006).


Documento: 13
Articulo: 227
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 2: De la estructura y articulacion

La Educacion Superior tendra una estructura organizativa abierta y flexible, permeable a la creacion de espacios y modalidades que faciliten la incorporacion de nuevas tecnologias educativas.


Documento: 13
Articulo: 228
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 2: De la estructura y articulacion

Todas las personas que aprueben la educacion secundaria pueden ingresar de manera libre e irrestricta a la ensenanza de grado en el nivel de educacion superior. Excepcionalmente, los mayores de veinticinco (25) anos que no reunan esa condicion, podran ingresar siempre que demuestren, a traves de las evaluaciones que las provincias, la Ciudad Autonoma de Buenos Aires o las universidades en su caso establezcan, que tienen preparacion o experiencia laboral acorde con los estudios que se proponen iniciar, asi como aptitudes y conocimientos suficientes para cursarlos satisfactoriamente. Este ingreso debe ser complementado mediante los procesos de nivelacion y orientacion profesional y vocacional que cada institucion de educacion superior debe constituir, pero que en ningun caso debe tener un caracter selectivo excluyente o discriminador. (Articulo sustituido por art. 4 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 229
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 2: De la estructura y articulacion

La articulacion entre las distintas instituciones que conforman el Sistema de Educacion Superior, que tienen por fin facilitar el cambio de modalidad, orientacion o carrera, la continuacion de los estudios en otros establecimientos, universitarios o no, asi como la reconversion de los estudios concluidos, se garantiza conforme a las siguientes responsabilidades y mecanismos: a) Las provincias y la Municipalidad de la Ciudad de Buenos Aires son las responsables de asegurar, en sus respectivos ambitos de competencia, la articulacion entre las instituciones de educacion superior que de ellas dependan; b) La articulacion entre institutos de educacion superior pertenecientes a distintas jurisdicciones, se regula por los mecanismos que estas acuerden en el seno del Consejo Federal de Cultura y Educacion; (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006) c) La articulacion entre institutos de educacion superior e instituciones universitarias, se establece mediante convenios entre ellas, o entre las instituciones Universitarias y la jurisdiccion correspondiente si asi lo establece la legislacion local; (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006). d) A los fines de la articulacion entre diferentes instituciones universitarias, el reconocimiento de los estudios parciales o asignaturas de las carreras de grado aprobados en cualquiera de esas instituciones, se hace por convenio entre ellas, conforme a los requisitos y pautas que se acuerdan en el consejo de Universidades.


Documento: 13
Articulo: 230
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 2: De la estructura y articulacion

A fin de hacer efectiva la articulacion entre institutos de educacion superior pertenecientes a distintas jurisdicciones prevista en el inciso b) del articulo anterior el Ministerio de Cultura y Educacion invitara al Consejo Federal de Cultura y Educacion a que integre una comision especial permanente, compuesta por un representante de cada una de las jurisdicciones. (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006).


Documento: 13
Articulo: 231
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 2: De la estructura y articulacion

La articulacion a nivel regional estara a cargo de los Consejos Regionales de Planificacion de la Educacion Superior, integrados por representantes de las instituciones universitarias y de los gobiernos provinciales de cada region.


Documento: 13
Articulo: 232
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 3: Derechos y obligaciones

Son derechos de los docentes de las instituciones estatales de educacion superior, sin perjuicio de lo dispuesto por la legislacion especifica: a) Acceder a la carrera academica mediante concurso publico y abierto de antecedentes y oposicion; b) Participar en el gobierno de la institucion a la que pertenecen, de acuerdo a las normas legales pertinentes; c) Actualizarse y perfeccionares de modo continuo a traves de la carrera academica; d) Participar en la actividad gremial.


Documento: 13
Articulo: 233
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 3: Derechos y obligaciones

Son deberes de los docentes de las instituciones estatales de educacion superior: a) Observar las normas que regulan el funcionamiento de la institucion a la que pertenecen; b) Participar en la vida de la institucion cumpliendo con responsabilidad su funcion docente, de investigacion y de servicio; c) Actualizarse en su formacion profesional y cumplir con las exigencias de perfeccionamiento que fije la carrera academica.


Documento: 13
Articulo: 234
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 3: Derechos y obligaciones

Los estudiantes de las instituciones estatales de educacion superior tienen derecho: a) Al acceso al sistema sin discriminaciones de ninguna naturaleza; b) A asociarse libremente en centros de estudiantes, federaciones nacionales y regionales, a elegir sus representantes y a participar en el gobierno y en la vida de la institucion, conforme a los estatutos, lo que establece la presente ley y, en su caso, las normas legales de las respectivas jurisdicciones; c) A obtener becas, creditos y otras formas de apoyo economico y social que garanticen la igualdad de oportunidades y posibilidades, particularmente para el acceso y permanencia en los estudios de grado, conforme a las normas que reglamenten la materia; d) A recibir, informacion para el adecuado uso de la oferta de servicios de educacion superior; e) A solicitar, cuando se encuentren en las situaciones previstas en los articulos 1o y 2o de la ley 20.596, la postergacion o adelanto de examenes o evaluaciones parciales o finales cuando las fechas previstas para los mismos se encuentren dentro del periodo de preparacion y/o participacion; f) Las personas con discapacidad, durante las evaluaciones, deberan contar con los servicios de interpretacion y los apoyos tecnicos necesarios y suficientes. (Inciso incorporado por art. 2 de la Ley N 25.573 B.O. 30/04/2002)


Documento: 13
Articulo: 235
Capitulo: TITULO II: DE LA EDUCACION SUPERIOR. CAPITULO 3: Derechos y obligaciones

Son obligaciones de los estudiantes de las instituciones estatales de educacion superior: a) Respetar los estatutos y reglamentaciones de la institucion en la que estudian; b) Observar las condiciones de estudio, investigacion, trabajo y convivencia que estipule la institucion a la que pertenecen; c) Respetar el disenso, las diferencias individuales, la creatividad personal y colectiva y el trabajo en equipo.


Documento: 13
Articulo: 236
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 1: De la responsabilidad jurisdiccional

Corresponde a las provincias y a la Municipalidad de la Ciudad de Buenos Aires el gobierno y organizacion de la educacion superior no universitaria en sus respectivos ambitos de competencia, asi como dictar normas que regulen la creacion, modificacion y cese de institutos de educacion superior y el establecimiento de las condiciones a que se ajustara su funcionamiento, todo ello en el marco de la Ley 24.195, de lo que establece la presente y de los correspondiente acuerdos federales. Las jurisdicciones atenderan en particular a las siguientes pautas: (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006). a) Estructurar los estudios en base a una organizacion curricular flexible y que facilite a sus egresados una salida laboral; b) Articular las carreras afines estableciendo en lo posible nucleos basicos comunes y regimenes flexibles de equivalencia y reconversion; c) Prever como parte de la formacion la realizacion de residencias programadas, sistemas de alternancia u otras formas de practicas supervisadas, que podran desarrollarse en las mismas instituciones o en entidades o empresas publicas o privadas; d) Tender a ampliar gradualmente el margen de autonomia de gestion de las instituciones respectivas, dentro de los lineamientos de la politica educativa jurisdiccional y federal; e) Prever que sus sistemas de estadistica e informacion educativa incluyan un componente especifico de educacion superior, que facilite el conocimiento, evaluacion y reajuste del respectivo subsistema; f) Establecer mecanismos de cooperacion interinstitucional y de reciproca asistencia tecnica y academica; g) Desarrollar modalidades regulares y sistematicas de evaluacion institucional, con arreglo a lo que estipula el articulo 25 de la presente ley.


Documento: 13
Articulo: 237
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 1: De la responsabilidad jurisdiccional

El Estado nacional podra apoyar programas de educacion superior no universitaria, que se caractericen por la singularidad de su oferta, por su sobresaliente nivel de excelencia, por su caracter experimental y/o por su incidencia local o regional.


Documento: 13
Articulo: 238
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 2: De las instituciones de educacion superior no universitaria

Los institutos de educacion superior, tienen por funciones basicas: (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006). a) Formar y capacitar para el ejercicio de la docencia en los niveles no universitarios del sistema educativo; b) Proporcionar formacion superior de caracter instrumental en las areas humanisticas, sociales, tecnico-profesionales y artisticas. Las mismas deberan estar vinculadas a la vida cultural y productiva local y regional.


Documento: 13
Articulo: 239
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 2: De las instituciones de educacion superior no universitaria

La formacion de docentes para los distintos niveles de la ensenanza no universitaria, debe realizarse en instituciones de formacion docente reconocidas, que integran la Red Federal de Formacion Docente Continua prevista en la ley 24.195 o en universidades que ofrezcan carreras con esa finalidad.


Documento: 13
Articulo: 240
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 2: De las instituciones de educacion superior no universitaria

Los institutos de educacion superior podran proporcionar formacion superior de ese caracter en el area de que se trate y/o actualizacion, reformulacion o adquisicion de nuevos conocimientos y competencias a nivel de postitulo. Podran asimismo desarrollar cursos, ciclos o actividades que respondan a las demandas de calificacion, formacion y reconversion laboral y profesional. (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006).


Documento: 13
Articulo: 241
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 2: De las instituciones de educacion superior no universitaria

El ingreso a la carrera docente en las instituciones de gestion estatal de educacion superior no universitaria se hara mediante concurso publico y abierto de antecedentes y oposicion, que garantice la idoneidad profesional para el desempeno de las tareas especificas. La estabilidad estara sujeta a un regimen de evaluacion y control de la gestion docente, y cuando sea el caso, a los requerimientos y caracteristicas de las carreras flexibles y a termino.


Documento: 13
Articulo: 242
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 2: De las instituciones de educacion superior no universitaria

Las provincias y la Municipalidad de la Ciudad de Buenos Aires arbitraran los medios necesarios para que sus instituciones de formacion docente garanticen el perfeccionamiento y la actualizacion de los docentes en actividad, tanto en los aspectos curriculares como en los pedagogicos e institucionales y promoveran el desarrollo de investigaciones educativas y la realizacion de experiencias innovadoras.


Documento: 13
Articulo: 243
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 2: De las instituciones de educacion superior no universitaria

Las instituciones de nivel superior no universitario que se creen o transformen, o las jurisdicciones a las que ellas pertenezcan, que acuerden con una o mas universidades del pais mecanismos de acreditacion de sus carreras o programas de formacion y capacitacion, podran denominarse colegios universitarios. Tales instituciones deberan estar estrechamente vinculadas a entidades de su zona de influencia y ofreceran carreras cortas flexibles y/o a termino, que faciliten la adquisicion de competencias profesionales y hagan posible su insercion laboral y/o la continuacion de los estudios en las universidades con las cuales hayan establecido acuerdos de articulacion.


Documento: 13
Articulo: 244
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 3: De los titulos y planes de estudio

Los planes de estudio de las instituciones de formacion docente de caracter no universitario, cuyos titulos habiliten para el ejercicio de la docencia en los niveles no universitarios del sistema, seran establecidos respetando los contenidos basicos comunes para la formacion docente que se acuerden en el seno del Consejo Federal de Cultura y Educacion. Su validez nacional estara sujeta al previo reconocimiento de dichos planes por la instancia que determine el referido Consejo. Igual criterio se seguira con los planes de estudio para la formacion humanistica, social, artistica o tecnico-profesional, cuyos titulos habiliten para continuar estudios en otros ciclos, niveles o establecimientos, o para el desempeno de actividades reguladas por el Estado, cuyo ejercicio pudiere poner en riesgo de modo directo la salud, la seguridad, los derechos o los, bienes de los habitantes.


Documento: 13
Articulo: 245
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 3: De los titulos y planes de estudio

Los titulos y certificados de perfeccionamiento y capacitacion docente expedidos por instituciones de educacion superior oficiales o privadas reconocidas, que respondan a las normas fijadas al respecto por el Consejo Federal de Cultura y Educacion, tendran validez nacional y seran reconocidos por todas las jurisdicciones. Tales titulos y certificados deberan ser expedidos en un plazo no mayor a los ciento veinte dias corridos contados a partir del inicio del tramite de solicitud de titulo. (Articulo sustituido por art. 2 de la Ley N 26.002 B.O. 5/1/2005).


Documento: 13
Articulo: 246
Capitulo: TITULO III: DE LA EDUCACION SUPERIOR NO UNIVERSITARIA. CAPITULO 4: De la evaluacion institucional

El Consejo Federal de Cultura y Educacion acordara la adopcion de criterios y bases comunes para la evaluacion de los institutos de educacion superior, en particular de aquellos que ofrezcan estudios cuyos titulos habiliten para el ejercicio de actividades reguladas por el Estado, que pudieren comprometer de modo directo el interes publico, estableciendo las condiciones y requisitos minimos a los que tales instituciones se deberan ajustar. (Expresion " instituciones de educacion superior no universitaria " sustituida por la expresion "institutos de educacion superior", por art. 133 de la Ley No 26.206, B.O. 28/12/2006). La evaluacion de la calidad de la formacion docente se realizara con arreglo a lo que establece la ley 24.195 en sus articulos 48 y 49.


Documento: 13
Articulo: 247
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 1: De las instituciones universitarias y sus funciones

La ensenanza superior universitaria estara a cargo de las universidades nacionales, de las universidades provinciales y privadas reconocidas por el Estado nacional y de los institutos universitarios estatales o privados reconocidos, todos los cuales integra el Sistema Universitario Nacional.


Documento: 13
Articulo: 248
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 1: De las instituciones universitarias y sus funciones

Las instituciones universitarias a que se refiere el articulo anterior, tienen por finalidad la generacion y comunicacion de conocimientos del mas alto nivel en un clima de libertad, justicia y solidaridad, ofreciendo una formacion cultural interdisciplinaria dirigida a la integracion del saber asi como una capacitacion cientifica y profesional especifica para las distintas carreras que en ellas se cursen, para beneficio del hombre y de la sociedad a la que pertenezcan. Las instituciones que responden a la denominacion de "Universidad" deben desarrollar su actividad en una variedad de areas disciplinarias no afines organicamente estructuradas en facultades, departamentos o unidades academicas equivalentes. Las instituciones que circunscriben su oferta academica a una sola area disciplinaria se denominan Institutos Universitarios.


Documento: 13
Articulo: 249
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 1: De las instituciones universitarias y sus funciones

Son funciones basicas de las instituciones universitarias: a) Formar y capacitar cientificos, profesionales, docentes y tecnicos, capaces de actuar con solidez profesional, responsabilidad, espiritu critico y reflexivo, mentalidad creadora, sentido etico y sensibilidad social, atendiendo a las demandas individuales, en particular de las personas con discapacidad, desventaja o marginalidad, y a los requerimientos nacionales y regionales; (Inciso sustituido por art. 3 de la Ley N 25.573 B.O. 30/04/2002) b) Promover y desarrollar la investigacion cientifica y tecnologia, los estudios humanisticos y las creaciones artisticas; c) Crear y difundir el conocimiento y la cultura en todas sus formas; d) Preservar la cultura nacional; e) Extender su accion y sus servicios a la comunidad, con el fin de contribuir a su desarrollo y transformacion, estudiando en particular los problemas nacionales y regionales y prestando asistencia cientifica y tecnica al Estado y a la comunidad.


Documento: 13
Articulo: 250
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 2: De la autonomia, su alcance y sus garantias

Las instituciones universitarias tendran autonomia academica e institucional, que comprende basicamente las siguientes atribuciones: a) Dictar y reformar sus estatutos, los que seran comunicados al Ministerio de Cultura y Educacion a los fines establecidos en el articulo 34 de la presente ley; b) Definir sus organos de gobierno, establecer sus funciones, decidir su integracion y elegir sus autoridades de acuerdo a lo que establezcan los estatutos y lo que prescribe la presente ley; c) Administrar sus bienes y recursos, conforme a sus estatutos y las leyes que regulan la materia; d) Crear carreras universitarias de grado y de posgrado; e) Formular y desarrollar planes de estudio, de investigacion cientifica y de extension y servicios a la comunidad incluyendo la ensenanza de la etica profesional y la formacion y capacitacion sobre la problematica de la discapacidad; (Inciso sustituido por art. 4 de la Ley N 25.573 B.O. 30/04/2002) f) Otorgar grados academicos y titulos habilitantes conforme a las condiciones que se establecen en la presente ley; g) Impartir ensenanza, con fines de experimentacion, de innovacion pedagogica o de practica profesional docente, en los niveles preuniversitarios, debiendo continuar en funcionamiento los establecimientos existentes actualmente que reunan dichas caracteristicas; h) Establecer el regimen de acceso, permanencia y promocion del personal docente y no docente; i) Designar y remover al personal; j) Establecer el regimen de admision, permanencia y promocion de los estudiantes, asi como el regimen de equivalencias; k) Revalidar, solo como atribucion de las universidades nacionales: titulos extranjeros; l) Fijar el regimen de convivencia; m) Desarrollar y participar en emprendimientos que favorezcan el avance y aplicacion de los conocimientos; n) Mantener relaciones de caracter educativo, cientifico-cultural con instituciones del pais y del extranjero; n) Reconocer oficialmente asociaciones de estudiantes, cumplidos que sean los requisitos que establezca la reglamentacion, lo que conferira a tales entidades personeria juridica.


Documento: 13
Articulo: 251
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 2: De la autonomia, su alcance y sus garantias

Las instituciones universitarias nacionales solo pueden ser intervenidas por el Honorable Congreso de la Nacion, o durante su receso y ad referendum del mismo, por el Poder Ejecutivo nacional por plazo determinado -no superior a los seis meses- y solo por alguna de las siguientes causales: a) Conflicto insoluble del o de la institucion que haga imposible su normal funcionamiento; b) Grave alteracion del orden publico; c) Manifiesto incumplimiento de la presente ley. La intervencion nunca podra menoscabar la autonomia academica.


Documento: 13
Articulo: 252
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 2: De la autonomia, su alcance y sus garantias

La fuerza publica no puede ingresar en las instituciones universitarias nacionales si no media orden escrita previa y fundada de juez competente o solicitud expresa de la autoridad universitaria legitimamente constituida.


Documento: 13
Articulo: 253
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 2: De la autonomia, su alcance y sus garantias

Contra las resoluciones definitivas de las instituciones universitarias nacionales impugnadas con fundamento en la interpretacion de las leyes de la Nacion, los estatutos y demas normas internas, solo podra interponerse recurso de apelacion ante la Camara Federal de Apelaciones con competencia en el lugar donde tiene su sede principal la institucion universitaria.


Documento: 13
Articulo: 254
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Las instituciones universitarias deben promover la excelencia y asegurar la libertad academica, la igualdad de oportunidades y posibilidades, la jerarquizacion docente, la corresponsabilidad de todos los miembros de la comunidad universitaria, asi como la convivencia pluralista de corrientes, teorias y lineas de investigacion. Cuando se trate de instituciones universitarias privadas, dicho pluralismo se entendera en un contexto de respeto a las cosmovisiones y valores expresamente declarados en sus estatutos.


Documento: 13
Articulo: 255
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Los estatutos, asi como sus modificaciones, entraran en vigencia a partir de su publicacion en el Boletin Oficial, debiendo ser comunicados al Ministerio de Cultura y Educacion a efectos de verificar su adecuacion a la presente ley y ordenar, en su caso, dicha publicacion. Si el Ministerio considerara que los mismos no se ajustan a la presente ley, debera plantear sus observaciones, dentro de los diez dias a contar de la comunicacion oficial ante la Camara Federal de Apelaciones, la que decidira en un plazo de veinte dias, sin mas tramite que una vista a la institucion universitaria. Si el Ministerio no planteara observaciones en la forma indicada dentro del plazo establecido, los estatutos se consideraran aprobados y deberan ser publicados. Los estatutos deben prever explicitamente: su sede principal, los objetivos de la institucion, su estructura organizativa, la integracion y funciones de los distintos organos de gobierno, asi como el regimen de la docencia y de la investigacion y pautas de administracion economico-financiera.


Documento: 13
Articulo: 256
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Para ingresar como alumno a las instituciones universitarias, sean estatales o privadas, debera reunirse como minimo la condicion prevista en el articulo 7o y cumplir con los demas requisitos del sistema de admision que cada institucion establezca.


Documento: 13
Articulo: 257
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Los docentes de todas las categorias deberan poseer titulo universitario de igual o superior nivel a aquel en el cual ejercen la docencia, requisito que solo se podra obviar con caracter estrictamente excepcional cuando se acrediten meritos sobresalientes. Quedan exceptuados de esta disposicion los ayudantes alumnos. Gradualmente se tendera a que el titulo maximo sea una condicion para acceder a la categoria de profesor universitario.


Documento: 13
Articulo: 258
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Las instituciones universitarias garantizaran el perfeccionamiento de sus docentes, que debera articularse con los requerimientos de la carrera academica. Dicho perfeccionamiento no se limitara a la capacitacion en el area cientifica o profesional especifica y en los aspectos pedagogicos, sino que incluira tambien el desarrollo de una adecuada formacion interdisciplinaria.


Documento: 13
Articulo: 259
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Las instituciones universitarias dictaran normas y estableceran acuerdos que faciliten la articulacion y equivalencias entre careras de una misma universidad o de instituciones universitarias distintas, conforme a las pautas a que se refiere el articulo 8o, inciso d).


Documento: 13
Articulo: 260
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

La formacion de posgrado se desarrollara exclusivamente en instituciones universitarias, y con las limitaciones previstas en el articulo 40 podra tambien desarrollarse en centros de investigacion e instituciones de formacion profesional superior de reconocido nivel y jerarquia, que hayan suscrito convenios con las universidades a esos efectos. Las carreras de posgrado sean especializacion, maestria o doctorado deberan ser acreditadas por la Comision Nacional de Evaluacion y Acreditacion Universitaria, o por entidades privadas que se constituyan con ese fin y que esten debidamente reconocidas por el Ministerio de Educacion, Ciencia y Tecnologia. (Articulo sustituido por art. 2 de la Ley N 25.754 B.O. 11/08/2003)


Documento: 13
Articulo: 261
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion I: Requisitos generales

Para acceder a la formacion de posgrado, el postulante debera contar con titulo universitario de grado o de nivel superior no universitario de cuatro (4) anos de duracion como minimo y reunir los prerequisitos que determine el Comite Academico o la autoridad equivalente, a fin de comprobar que su formacion resulte compatible con las exigencias del posgrado al que aspira. En casos excepcionales de postulantes que se encuentren fuera de los terminos precedentes, podran ser admitidos siempre que demuestren, a traves de las evaluaciones y los requisitos que la respectiva universidad establezca, poseer preparacion y experiencia laboral acorde con los estudios de posgrado que se proponen iniciar asi como aptitudes y conocimientos suficientes para cursarlos satisfactoriamente. En todos los casos la admision y la obtencion del titulo de posgrado no acredita de manera alguna el titulo de grado anterior correspondiente al mismo. (Articulo incorporado por art. 2 de la Ley N 25.754 B.O. 11/08/2003)


Documento: 13
Articulo: 262
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion II: Regimen de titulos

Corresponde exclusivamente a las instituciones universitarias otorgar el titulo de grado de licenciado y titulos profesionales equivalentes, asi como los titulos de posgrado de magister y doctor, los que deberan ser expedidos en un plazo no mayor a los ciento veinte dias corridos contados a partir del inicio del tramite de solicitud de titulo. (Articulo sustituido por art. 1 de la Ley N 26.002 B.O. 5/1/2005).


Documento: 13
Articulo: 263
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion II: Regimen de titulos

El reconocimiento oficial de los titulos que expidan las instituciones universitarias sera otorgado por el Ministerio de Cultura y Educacion. Los titulos oficialmente reconocidos tendran validez nacional.


Documento: 13
Articulo: 264
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion II: Regimen de titulos

Los titulos con reconocimiento oficial certificaran la formacion academica recibida y habilitaran para el ejercicio profesional respectivo en todo el territorio nacional, sin perjuicio del poder de policia sobre las profesiones que corresponde a las provincias. Los conocimientos y capacidades que tales titulos certifican, asi como las actividades para las que tienen competencia sus poseedores, seran fijados y dados a conocer por las instituciones universitarias, debiendo los respectivos planes de estudio respetar la carga horaria minima que para ello fije el Ministerio de Cultura y Educacion, en acuerdo con el Consejo de Universidades.


Documento: 13
Articulo: 265
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion II: Regimen de titulos

Cuando se trate de titulos correspondientes a profesiones reguladas por el Estado, cuyo ejercicio pudiera comprometer el interes publico poniendo en riesgo de modo directo la salud, la seguridad, los derechos, los bienes o la formacion de los habitantes, se requerira que se respeten, ademas de la carga horaria a la que hace referencia el articulo anterior, los siguientes requisitos: a) Los planes de estudio deberan tener en cuenta los contenidos curriculares basicos y los criterios sobre intensidad de la formacion practica que establezca el Ministerio de Cultura y Educacion, en acuerdo con el Consejo de Universidades; b) Las carreras respectivas deberan ser acreditadas periodicamente por la Comision Nacional de Evaluacion y Acreditacion Universitaria o por entidades privadas constituidas con ese fin debidamente reconocidas. El Ministerio de Cultura y Educacion determinara con criterio restrictivo, en acuerdo con el Consejo de Universidades, la nomina de tales titulos, asi como las actividades profesionales reservadas exclusivamente para ellos.


Documento: 13
Articulo: 266
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion III: Evaluacion y acreditacion

Las instituciones universitarias deberan asegurar el funcionamiento de instancias internas de evaluacion institucional, que tendran por objeto analizar los logros y dificultades en el cumplimiento de sus funciones, asi como sugerir medidas para su mejoramiento. Las autoevaluaciones se complementaran con evaluaciones externas. que se haran como minimo cada seis (6) anos, en el marco de los objetivos definidos por cada institucion. Abarcaran las funciones de docencia, investigacion y extension, y en el caso de las instituciones universitarias nacionales, tambien la gestion institucional. Las evaluaciones externas estaran a cargo de la Comision Nacional de Evaluacion y Acreditacion Universitaria o de entidades privadas constituidas con ese fin, conforme se preve en el articulo 45, en ambos casos con la participacion de pares academicos de reconocida competencia. Las recomendaciones para el mejoramiento institucional que surjan de las evaluaciones tendran caracter publico.


Documento: 13
Articulo: 267
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion III: Evaluacion y acreditacion

Las entidades privadas que se constituyan con fines de evaluacion y acreditacion de instituciones universitarias, deberan contar con el reconocimiento del Ministerio de Cultura y Educacion, previo dictamen de la Comision Nacional de Evaluacion y Acreditacion Universitaria. Los patrones y estandares para los procesos de acreditacion, seran los que establezca el Ministerio previa consulta con el Consejo de Universidades.


Documento: 13
Articulo: 268
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion III: Evaluacion y acreditacion

La Comision Nacional de Evaluacion y Acreditacion Universitaria es un organismo descentralizado, que funciona en jurisdiccion del Ministerio de Cultura y Educacion. y que tiene por funciones: a) Coordinar y llevar adelante la evaluacion externa prevista en el articulo 44; b) Acreditar las carreras de grado a que se refiere el articulo 43, asi como las carreras de posgrado, cualquiera sea el ambito en que se desarrollen, conforme a los estandares que establezca el Ministerio de Cultura y Educacion en consulta con el Consejo de Universidades; c) Pronunciarse sobre la consistencia y viabilidad del proyecto institucional que se requiere para que el Ministerio de Cultura y Educacion autorice la puesta en marcha de una nueva institucion universitaria nacional con posterioridad a su creacion o el reconocimiento de una institucion universitaria provincial; d) Preparar los informes requeridos para otorgar la autorizacion provisoria y el reconocimiento definitivo de las instituciones universitarias privadas, asi como los informes en base a los cuales se evaluara el periodo de funcionamiento provisorio de dichas instituciones.


Documento: 13
Articulo: 269
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 3: De las condiciones para su funcionamiento. Seccion III: Evaluacion y acreditacion

La Comision Nacional de Evaluacion y Acreditacion Universitaria estara integrada por doce (12) miembros, designados por el Poder Ejecutivo nacional a propuesta de los siguientes organismos: tres (3) por el Consejo Interuniversitario Nacional, uno (1) por el Consejo de Rectores de Universidades Privadas, uno (1) por la Academia Nacional de Educacion, tres (3) por cada una de las Camaras del Honorable Congreso de la Nacion, y uno (1) por el Ministerio de Cultura y Educacion. Duraran en sus funciones cuatro anos, con sistema de renovacion parcial. En todos los casos debera tratarse de personalidades de reconocida jerarquia academica y cientifica. La Comision contara con presupuesto propio.


Documento: 13
Articulo: 270
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion I: Creacion y bases organizativas

Las instituciones universitarias nacionales son personas juridicas de derecho publico, que solo pueden crearse por ley de la Nacion, con prevision del credito presupuestario correspondiente y en base a un estudio de factibilidad que avale la iniciativa. El cese de tales instituciones se hara tambien por ley. Tanto la creacion como el cierre requeriran informe previo del Consejo Interuniversitario Nacional.


Documento: 13
Articulo: 271
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion I: Creacion y bases organizativas

Creada una institucion universitaria, el Ministerio de Cultura y Educacion designara un rector-organizador, con las atribuciones propias del cargo y las que normalmente corresponden al Consejo Superior. El rector-organizador conducira el proceso de formulacion del proyecto institucional y del proyecto de estatuto provisorio y los pondra a consideracion del Ministerio de Cultura y Educacion, en el primer caso para su analisis y remision a la Comision Nacional de Evaluacion y Acreditacion Universitaria, y en el segundo, a los fines de su aprobacion y posterior publicacion Producido el informe de la Comision, y adecuandose el proyecto de estatuto a las normas de la presente ley, procedera el Ministerio de Cultura y Educacion a autorizar la puesta en marcha de la nueva institucion, la que debera quedar normalizada en un plazo no superior a los cuatro (4) anos a partir de su creacion.


Documento: 13
Articulo: 272
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion I: Creacion y bases organizativas

Cada institucion universitaria nacional dictara normas sobre regularidad en los estudios que establezcan las condiciones academicas exigibles. (Articulo sustituido por art. 5 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 273
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion I: Creacion y bases organizativas

El ingreso a la carrera academica universitaria se hara mediante concurso publico y abierto de antecedentes y oposicion, debiendose asegurar la constitucion de jurados integrados por profesores por concurso, o excepcionalmente por personas de idoneidad indiscutible aunque no reunan esa condicion, que garanticen la mayor imparcialidad y el maximo rigor academico. Con caracter excepcional, las universidades e institutos universitarios nacionales podran contratar, al margen del regimen de concursos y solo por tiempo determinado, a personalidades de reconocido prestigio y meritos academicos sobresalientes para que desarrollen cursos, seminarios o actividades similares. Podran igualmente prever la designacion temporaria de docentes interinos, cuando ello sea imprescindible y mientras se sustancia el correspondiente concurso. Los docentes designados por concurso deberan representar un porcentaje no inferior al setenta por ciento (70%) de las respectivas plantas de cada institucion universitaria.


Documento: 13
Articulo: 274
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion II: Organos de gobierno

Los estatutos de las instituciones universitarias nacionales deben prever sus organos de gobierno, tanto colegiados como unipersonales, asi como su composicion y atribuciones. Los organos colegiados tendran basicamente funciones normativas generales, de definicion de politicas y de control en sus respectivos ambitos, en tanto los unipersonales tendran funciones ejecutivas.


Documento: 13
Articulo: 275
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion II: Organos de gobierno

Los organos colegiados de gobierno estaran integrados de acuerdo a lo que determinen los estatutos de cada universidad, los que deberan asegurar: a) Que el claustro docente tenga la mayor representacion relativa, que no podra ser inferior al cincuenta por ciento (50%) de la totalidad de sus miembros; b) Que los representantes de los estudiantes sean alumnos regulares y tengan aprobado por lo menos el treinta por ciento (30%) del total de asignaturas de la carrera que cursan; c) Que el personal no docente tenga representacion en dichos cuerpos con el alcance que determine cada institucion; d) Que los graduados, en caso de ser incorporados a los cuerpos colegiados, puedan elegir y ser elegidos si no tienen relacion de dependencia con la institucion universitaria. Los decanos o autoridades docentes equivalentes seran miembros natos del Consejo Superior u organo que cumpla similares funciones. Podra extenderse la misma consideracion a los directores de carrera de caracter electivo que integren los cuerpos academicos, en las instituciones que por su estructura organizativa prevean dichos cargos.


Documento: 13
Articulo: 276
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion II: Organos de gobierno

El rector o presidente, el vicerector o vicepresidente y los titulares de los demas organos unipersonales de gobierno, duraran en sus funciones tres (3) anos como minimo. El cargo de rector o presidente sera de dedicacion exclusiva y para acceder a el se requerira ser o haber sido profesor por concurso de una universidad nacional.


Documento: 13
Articulo: 277
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion II: Organos de gobierno

Los representantes de los docentes, que deberan haber accedido a sus cargos por concurso, seran elegidos por docentes que reunan igual calidad. Los representantes estudiantiles seran elegidos por sus pares, siempre que estos tengan el rendimiento academico minimo que establece el articulo 50.


Documento: 13
Articulo: 278
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion II: Organos de gobierno

Los estatutos podran prever la constitucion de un consejo social, en el que esten representados los distintos sectores e intereses de la comunidad local, con la mision de cooperar con la institucion universitaria en su articulacion con el medio en que esta inserta. Podra igualmente preverse que el Consejo Social este representado en los organos colegiados de la institucion.


Documento: 13
Articulo: 279
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion II: Organos de gobierno

Los estatutos preveran la constitucion de un tribunal universitario, que tendra por funcion sustanciar juicios academicos y entender en toda cuestion etico-disciplinaria en que estuviere involucrado personal docente. Estara integrado por profesores emeritos o consultos, o por profesores por concurso que tengan una antiguedad en la docencia universitaria de por lo menos diez (10) anos.


Documento: 13
Articulo: 280
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion III: Sostenimiento y regimen economico financiero

El aporte del Estado nacional para las instituciones de educacion superior universitaria de gestion estatal no puede ser disminuido ni reemplazado en ningun caso mediante recursos adicionales provenientes de otras fuentes no contempladas en el presupuesto anual general de la administracion publica nacional. (Articulo sustituido por art. 6 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 281
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion III: Sostenimiento y regimen economico financiero

Las instituciones universitarias nacionales tienen autarquia economico-financiera que ejerceran dentro del regimen de la ley 24.156, de administracion financiera y sistemas de control del sector publico nacional. En ese marco corresponde a dichas instituciones: a) Administrar su patrimonio y aprobar su presupuesto. Los recursos no utilizados al cierre de cada ejercicio se transferiran automaticamente al siguiente; b) Fijar su regimen salarial y de administracion de personal; c) Podran dictar normas relativas a la generacion de recursos adicionales a los aportes del Tesoro nacional, mediante la venta de bienes, productos, derechos o servicios, subsidios, contribuciones, herencias, derechos o tasas por los servicios que presten, asi como todo otro recurso que pudiera corresponderles por cualquier titulo o actividad. Los recursos adicionales que provinieren de contribuciones deberan destinarse prioritariamente a becas, prestamos, subsidios o creditos u otro tipo de ayuda estudiantil y apoyo didactico; estos recursos adicionales no podran utilizarse para financiar gastos corrientes. Los sistemas de becas, prestamos u otro tipo de ayuda estaran fundamentalmente destinados a aquellos estudiantes que por razones economicas no pudieran acceder o continuar los estudios universitarios, de forma tal que nadie se vea imposibilitado por ese motivo de cursar tales estudios; d) Garantizar el normal desenvolvimiento de sus unidades asistenciales, asegurandoles el manejo descentralizado de los fondos que ellas generen, con acuerdo a las normas que dicten sus consejos superiores y a la legislacion vigente; e) Constituir personas juridicas de derecho publico o privado, o participar en ellas, no requiriendose adoptar una forma juridica diferente para acceder a los beneficios de la ley 23.877, de promocion y fomento de la innovacion tecnologica; f) Aplicar el regimen general de contrataciones, de responsabilidad patrimonial y de gestion de bienes reales, con las excepciones que establezca la reglamentacion. El rector y los miembros del Consejo Superior de las Instituciones Universitarias Nacionales seran responsables de su administracion segun su participacion, debiendo responder en los terminos y con los alcances previstos en los articulos 130 y 131 de la ley 24.156. En ningun caso el Estado nacional respondera por las obligaciones asumidas por las instituciones universitarias que importen un perjuicio para el Tesoro nacional. (Articulo sustituido por art. 7 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 282
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion III: Sostenimiento y regimen economico financiero

El control administrativo externo de las instituciones de educacion superior universitarias de gestion estatal es competencia directa e indelegable de la Auditoria General de la Nacion que, a tales efectos, dispondra de un area especifica con los recursos humanos y materiales adecuados para llevar a cabo esta tarea. Todas las instituciones de educacion superior universitarias de gestion estatal deben generar mecanismos de auditoria interna que garanticen transparencia en el uso de los bienes y recursos. (Articulo incorporado por art. 8 de la Ley N 27.204 B.O. 11/11/2015)


Documento: 13
Articulo: 283
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion III: Sostenimiento y regimen economico financiero

Las instituciones universitarias nacionales podran promover la constitucion de fundaciones, sociedades u otras formas de asociacion civil, destinada a apoyar su labor, a facilitar las relaciones con el medio, a dar respuesta a sus necesidades y a promover las condiciones necesaria para el cumplimiento de sus fines y objetivos.


Documento: 13
Articulo: 284
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 4: De las instituciones universitarias nacionales. Seccion III: Sostenimiento y regimen economico financiero

El Congreso Nacional debe disponer de la partida presupuestaria anual correspondiente al nivel de educacion de superior, de un porcentaje que sera destinado a becas y subsidios en ese nivel. (Expresion "otorgables por el Congreso de la Nacion y ejecutables en base a lo dispuesto por el articulo 75, inciso 19 de la Constitucion Nacional, por parte del Tesoro de la Nacion" vetada por art. 2o del Decreto No 268/95 B.O. 10/08/1995).


Documento: 13
Articulo: 285
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

Las instituciones universitarias privadas deberan constituirse sin fines de lucro, obteniendo personeria juridica como asociacion civil o fundacion. Las mismas seran autorizadas por decreto del Poder Ejecutivo Nacional, que admitira su funcionamiento provisorio por un lapso de seis (6) anos, previo informe favorable de la Comision Nacional de Evaluacion y Acreditacion Universitaria, y con expresa indicacion de las carreras, grados y titulos que la institucion puede ofrecer y expedir.


Documento: 13
Articulo: 286
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

El informe de la Comision Nacional de Evaluacion y Acreditacion Universitaria a que se refiere el articulo anterior, se fundamentara en la consideracion de los siguientes criterios: a) La responsabilidad moral, financiera y economica de los integrantes de las asociaciones o fundaciones; b) La viabilidad y consistencia del proyecto institucional y academico asi como su adecuacion a los principios y normas de la presente ley; c) El nivel academico del cuerpo de profesores con el que se contara inicialmente, su trayectoria en investigacion cientifica y en docencia universitaria; d) La calidad y actualizacion de los planes de ensenanza e investigacion propuestos; e) Los medios economicos, el equipamiento y la infraestructura de que efectivamente se dispongan para posibilitar el cumplimiento de sus funciones de docencia, investigacion y extension; f) Su vinculacion internacional y la posibilidad de concretar acuerdos y convenios con otros centros universitarios del mundo.


Documento: 13
Articulo: 287
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

Durante el lapso de funcionamiento provisorio: a) El Ministerio de Cultura y Educacion hara un seguimiento de la nueva Institucion a fin de evaluar, en base a informes de la Comision Nacional de Evaluacion y Acreditacion Universitaria, su nivel academico y el grado de cumplimiento de sus objetivos y planes de accion; b) Toda modificacion de los estatutos creacion de nuevas carreras cambio de planes de estudio o modificacion de los mismos, requerira autorizacion del citado Ministerio; c) En todo documento oficial o publicidad que realicen las instituciones deberan dejar constancia expresa del caracter precario de la autorizacion con que operan. El incumplimiento de las exigencias previstas en los incisos b) y c) dara lugar a la aplicacion de sanciones conforme lo establezca la reglamentacion de la presente ley, la que podra llegar al retiro de la autorizacion provisoria concedida.


Documento: 13
Articulo: 288
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

Cumplido el lapso de seis (6) anos de funcionamiento provisorio contados a partir de la autorizacion correspondiente, el establecimiento podra solicitar el reconocimiento definitivo para operar como institucion universitaria privada, el que se otorgara por decreto del Poder Ejecutivo nacional previo informe favorable de la Comision Nacional de Evaluacion y Acreditacion Universitaria. El Ministerio de Cultura y Educacion fiscalizara el funcionamiento de dichas instituciones con el objeto de verificar si cumplen las condiciones bajo las cuales estan autorizadas a fusionar. Su incumplimiento dara lugar a la aplicacion de sanciones conforme lo establezca la reglamentacion de la presente ley, la que podra llegar hasta la clausura definitiva.


Documento: 13
Articulo: 289
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

El Estado nacional podra acordar a las instituciones con reconocimiento definitivo que lo soliciten, apoyo economico para el desarrollo de proyectos de investigacion que se generen en las mismas, sujeto ello a los mecanismos de evaluacion y a los criterios de elegibilidad que rijan para todo el sistema.


Documento: 13
Articulo: 290
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

Las resoluciones denegatorias del reconocimiento definitivo, asi como aquellas que dispongan su retiro o el de la autorizacion provisoria, seran recurribles ante la Camara Federal correspondiente a la jurisdiccion de la institucion de que se trate, dentro de los quince (15) dias habiles de notificada la decision que se recurre.


Documento: 13
Articulo: 291
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 5: De las instituciones universitarias privadas

Los establecimientos privados cuya creacion no hubiere sido autorizada conforme a las normas legales pertinentes no podran usar denominaciones ni expedir diplomas, titulos o grados de caracter universitario. La violacion de esta norma dara lugar a la aplicacion de sanciones conforme lo establezca la reglamentacion de la presente ley, la que podra llegar a la clausura inmediata y definitiva de la entidad y a la inhabilitacion de los responsables para ejercer la docencia, asi como para desempenar la funcion publica o integrar organos de gobierno de asociaciones civiles dedicadas a la educacion superior.


Documento: 13
Articulo: 292
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 6: De las instituciones universitarias provinciales

Los titulos y grados otorgados por las instituciones universitarias provinciales tendran los efectos legales previstos en la presente ley, en particular los establecidos en los articulos 41 y 42, cuando tales instituciones: a) Hayan obtenido el correspondiente reconocimiento del Poder Ejecutivo Nacional, el que podra otorgarse previo informe de la Comision Nacional de Evaluacion y Acreditacion Universitaria, siguiendo las pautas previstas en el articulo 63; b) Se ajusten a las normas de los capitulos 1, 2, 3 y 4 del presente titulo, en tanto su aplicacion a estas instituciones no vulnere las autonomias provinciales y conforme a las especificaciones que establezca la reglamentacion.


Documento: 13
Articulo: 293
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 7: Del gobierno y coordinacion del sistema universitario

Corresponde al Ministerio de Cultura y Educacion la formulacion de las politicas generales en materia universitaria, asegurando la participacion de los organos de coordinacion y consulta previstos en la presente ley y respetando el regimen de autonomia establecido para las instituciones universitarias.


Documento: 13
Articulo: 294
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 7: Del gobierno y coordinacion del sistema universitario

Seran organos de coordinacion y consulta del sistema universitario, en sus respectivos ambitos, el Consejo de Universidades, el Consejo Interuniversitario Nacional, el Consejo de Rectores de Universidades Privadas y los Consejos Regionales de Planificacion de la Educacion Superior.


Documento: 13
Articulo: 295
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 7: Del gobierno y coordinacion del sistema universitario

El Consejo de Universidades sera presidido por el Ministro de Cultura y Educacion o por quien este designe con categoria no inferior a Secretario, y estara integrado por el Comite Ejecutivo del Consejo Interuniversitario Nacional, por la Comision Directiva del Consejo de Rectores de Universidades Privadas, por un representante de cada Consejo Regional de Planificacion de la Educacion Superior que debera ser rector de una institucion universitaria y por un representante del Consejo Federal de Cultura y Educacion. Seran sus funciones: a) Proponer la definicion de politicas y estrategias de desarrollo universitario, promover la cooperacion entre las instituciones universitarias, asi como la adopcion de pautas para la coordinacion del sistema universitario; b) Pronunciarse en aquellos asuntos sobre los cuales se requiera su intervencion conforme a la presente ley; c) Acordar con el Consejo Federal de Cultura y Educacion criterios y pautas para la articulacion entre las instituciones educativas de nivel superior; d) Expedirse sobre otros asuntos que se les remita en consulta por la via correspondiente.


Documento: 13
Articulo: 296
Capitulo: TITULO IV: DE LA EDUCACION SUPERIOR UNIVERSITARIA. CAPITULO 7: Del gobierno y coordinacion del sistema universitario

El Consejo Interuniversitario Nacional estara integrado por los rectores o presidentes de las instituciones universitarias nacionales y provinciales reconocidas por la Nacion, que esten definitivamente organizadas, y el Consejo de Rectores de Universidades Privadas estara integrado por los rectores o presidentes de las instituciones universitarias privadas. Dichos consejos tendran por funciones: a) Coordinar los planes y actividades en materia academica, de investigacion cientifica y de extension entre las instituciones universitarias de sus respectivos ambitos; b) Ser organos de consulta en las materias y cuestiones que preve la presente ley; c) Participar en el Consejo de Universidades. Cada Consejo se dara su propio reglamento conforme al cual regulara su funcionamiento interno.


Documento: 13
Articulo: 297
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

La presente ley autoriza la creacion y funcionamiento de otras modalidades de organizacion universitaria previstas en el articulo 24 de la ley 24.195 que respondan a modelos diferenciados de diseno de organizacion institucional y de metodologia pedagogica, previa evaluacion de su factibilidad y de la calidad de su oferta academica, sujeto todo ello a la reglamentacion que oportunamente dicte el Poder Ejecutivo nacional. Dichas instituciones, que tendran por principal finalidad favorecer el desarrollo de la educacion superior mediante una oferta diversificada pero de nivel equivalente a la del resto de las universidades, seran creadas o autorizadas segun corresponda conforme a las previsiones de los articulos 48 y 62 de la presente ley y seran sometidas al regimen de titulos y de evaluacion establecido en ella.


Documento: 13
Articulo: 298
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Las instituciones universitarias reguladas de conformidad con la presente ley, podran ser eximidas parcial o totalmente de impuestos y contribuciones previsionales de caracter nacional, mediante decreto del Poder Ejecutivo nacional.


Documento: 13
Articulo: 299
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Cuando una carrera que requiera acreditacion no la obtuviere, por no reunir los requisitos y estandares minimos previamente establecidos, la Comision Nacional de Evaluacion y Acreditacion Universitaria podra recomendar que se suspenda la inscripcion de nuevos alumnos en la misma, hasta que se subsanen las deficiencias encontradas, debiendose resguardar los derechos de los alumnos ya inscriptos que se encontraren cursando dicha carrera.


Documento: 13
Articulo: 300
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Las instituciones constituidas conforme al regimen del articulo 16 de la ley 17.778. que quedan por esta ley categorizadas como institutos universitarios, estableceran su sistema de gobierno conforme a sus propios regimenes institucionales, no siendoles de aplicacion las normas sobre autonomia y sobre gobierno de las instituciones universitarias nacionales que preve la presente ley.


Documento: 13
Articulo: 301
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Las instituciones universitarias nacionales deberan adecuar sus plantas docentes de acuerdo a lo previsto en el segundo parrafo del articulo 51 de la presente ley dentro del plazo de tres (3) anos contados a partir de la promulgacion de esta y de hasta diez (10) anos para las creadas a partir del 10 de diciembre de 1983. En estos casos, los docentes interinos con mas de dos (2) anos de antiguedad continuados podran ejercer los derechos consagrados en el articulo 55 de la presente ley.


Documento: 13
Articulo: 302
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Las instituciones universitarias nacionales adecuaran sus estatutos a las disposiciones de la presente ley, dentro del plazo de ciento ochenta (180) dias contados a partir de la promulgacion de esta.


Documento: 13
Articulo: 303
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Los titulares de los organos colegiados y unipersonales de gobierno de las instituciones universitarias nacionales, elegidos de acuerdo a los estatutos vigentes al momento de la sancion de la presente ley, continuaran en sus cargos hasta la finalizacion de sus respectivos mandatos. Sin perjuicio de ello, las autoridades universitarias adecuaran la integracion de sus organos colegiados de gobierno, a fin de que se respete la proporcion establecida en el articulo 53, inciso a), en un plazo de ciento ochenta (180) dias contados a partir de la fecha de publicacion de los nuevos estatutos, los que deberan contemplar normas que faciliten la transicion.


Documento: 13
Articulo: 304
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Las instituciones universitarias que al presente ostenten el nombre de universidad, por haber sido creadas o autorizadas con esa denominacion y que por sus caracteristicas deban encuadrarse en lo que por esta ley se denomina institutos universitarios, tendran un plazo de un (1) ano contado a partir de la promulgacion de la presente para solicitar la nueva categorizacion.


Documento: 13
Articulo: 305
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

La Universidad Tecnologica Nacional, en razon de su significacion en la vida universitaria del pais, conservara su denominacion y categoria institucional actual.


Documento: 13
Articulo: 306
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Los centros de investigacion e instituciones de formacion profesional superior que no sean universitarios y que a la fecha desarrollen actividades de posgrado, tendran un plazo de dos (2) anos para adecuarse a la nueva legislacion. Durante ese periodo estaran no obstante sometidos a la fiscalizacion del Ministerio de Cultura y Educacion y al regimen de acreditacion previsto en el articulo 39 de la presente ley.


Documento: 13
Articulo: 307
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

El Poder Ejecutivo nacional no podra implementar la organizacion de nuevas instituciones universitarias nacionales, ni disponer la autorizacion provisoria o el reconocimiento definitivo de instituciones universitarias privadas, hasta tanto se constituya el organo de evaluacion y acreditacion que debe pronunciarse sobre el particular, previsto en la presente ley.


Documento: 13
Articulo: 308
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Sustituyese el inciso 11) del articulo 21 de la Ley de Ministerios (t. o.1992) por el siguiente transcripto: Entender en la habilitacion de titulos profesionales con validez nacional.


Documento: 13
Articulo: 309
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Modificanse los siguientes articulos de la ley 24.195: a) Articulo 10, inciso e), y articulos 25 y 26, donde dice: "cuaternario", dira: "de posgrado". b) Articulo 54: donde dice "un representante del Consejo Interuniversitario Nacional", dira: "y tres representantes del Consejo de Universidades". c) Articulo 57: inciso a), donde dice: "y el representante del Consejo Interuniversitario Nacional", dira: "y los representantes del Consejo de Universidades". d) Articulo 58: inciso a), donde dice: "y el Consejo Interuniversitario Nacional", dira: "y el Consejo de Universidades".


Documento: 13
Articulo: 310
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Deroganse las leyes 17.604, 17.778, 23.068 y 23.569, asi como toda otra disposicion que se oponga a la presente.


Documento: 13
Articulo: 311
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Todas las normas que eximen de impuestos, tasas y contribuciones a las universidades nacionales al momento de la promulgacion de la presente ley, continuaran vigentes.


Documento: 13
Articulo: 312
Capitulo: TITULO V: DISPOSICIONES COMPLEMENTARIAS Y TRANSITORIAS

Comuniquese al Poder Ejecutivo.  CARLOS A. ROMERO.  CARLOS F. RUCKAUF.  Juan Estrada.  Edgardo Piuzzi.


Documento: 14
Articulo: 313
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

La presente ley establece el Sistema Educativo Provincial y regula el ejercicio del derecho humano, personal y social de ensenar y aprender consagrado constitucionalmente para todos los habitantes del territorio entrerriano.


Documento: 14
Articulo: 314
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial garantiza como prioridad la educacion integral, permanente y el acceso a la informacion y al conocimiento para todos los habitantes.


Documento: 14
Articulo: 315
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial tiene la responsabilidad principal, imprescriptible, intransferible e indelegable, de garantizar una educacion de caracter publica, estatal, gratuita y laica en todos los niveles y establecer la politica educativa y los fines y objetivos de la educacion en el marco de la ley de Educacion Nacional No 26.206.


Documento: 14
Articulo: 316
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial, a traves del Consejo General de Educacion, garantiza el acceso, permanencia, reingreso y egreso a la educacion obligatoria, en igualdad de condiciones y posibilidades, sin ningun tipo de discriminacion, reconociendo como responsables de la educacion a la familia como agente natural y primario y las confesiones religiosas reconocidas, los municipios y las organizaciones cooperativas y sociales.


Documento: 14
Articulo: 317
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial instrumentara politicas publicas que garanticen la erradicacion del analfabetismo, la inclusion educativa y cultural en todos los sectores priorizando la poblacion en situacion de vulnerabilidad educativa.


Documento: 14
Articulo: 318
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial, a traves del Consejo General de Educacion, garantiza el ejercicio pleno, efectivo y permanente a la educacion y a los derechos reconocidos en la Ley Nacional de Proteccion Integral de los Derechos de las ninas, ninos y adolescentes No 26.061 y la Ley Provincial de Proteccion Integral de los Derechos de los Ninos, Adolescentes y la Familia No 9861.


Documento: 14
Articulo: 319
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial asegura la creacion, el funcionamiento y sostenimiento de instituciones educativas publicas de gestion estatal en todos los niveles y modalidades.


Documento: 14
Articulo: 320
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial asegura el reconocimiento, la autorizacion y sostenimiento en los porcentajes establecidos por la reglamentacion y la supervision de establecimientos educativos publicos de gestion privada.


Documento: 14
Articulo: 321
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Consejo General de Educacion promovera programas especiales dirigidos a prevenir y asistir las desigualdades educativas de los sectores socialmente desfavorecidos de ninos y ninas, en coordinacion con otros organismos del Estado nacional, provincial y municipal, especialmente el Ministerio de Salud y Desarrollo Social y Organizaciones no gubernamentales.


Documento: 14
Articulo: 322
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Consejo General de Educacion garantiza en todos los niveles y modalidades del sistema educativo el desarrollo de una perspectiva pedagogica intercultural bilingue en articulacion con la educacion comun en el marco del derecho constitucional de las comunidades originarias.


Documento: 14
Articulo: 323
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Consejo General de Educacion aprobara los lineamientos curriculares para cada nivel educativo obligatorio integrandose de manera transversal, educacion con cultura, derechos humanos, culturas ancestrales, patrimonio tangible e intangible, cooperativismo y mutualismo, educacion para la paz, la resolucion pacifica de conflictos, trabajo, ciencia y tecnologia y educacion ambiental.


Documento: 14
Articulo: 324
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO I: Derechos, obligaciones y garantias

El Estado Provincial garantiza el financiamiento del sistema educativo conforme a lo establecido en la presente ley.


Documento: 14
Articulo: 325
Capitulo: TITULO I: DISPOSICIONES GENERALES. CAPITULO II: Fines y objetivos de la Educacion Entrerriana

La Educacion Entrerriana persigue los siguientes fines y objetivos: a) Contribuir a la formacion integral de las personas. b) Fomentar la practica de valores, de la verdad, libertad, igualdad, justicia, solidaridad, respeto a la diversidad, a la pluralidad y a la busqueda de consensos. c) Promover la educacion en derechos humanos y formacion ciudadana como principios fundantes de la democracia. d) Promover la formacion de ciudadanos activos que contribuyan a la consolidacion de la identidad nacional, a la democracia politica, social y cultural, a la valorizacion y preservacion del patrimonio natural y cultural, al desarrollo economico de la Provincia y la Nacion en un proceso de integracion regional y latinoamericana. e) Brindar una educacion entendida en terminos de justicia social, con igualdad de oportunidades y posibilidades, regionalmente equilibrada en todo el territorio provincial. f) Promover la formacion, produccion y distribucion de conocimientos, la creatividad y el pensamiento critico, la cultura del esfuerzo, el trabajo solidario, la responsabilidad por los resultados y la defensa de los derechos humanos. g) Brindar a todos y todas oportunidades de acceso, permanencia, movilidad, reingreso y egreso de los diferentes niveles del sistema educativo, en condiciones de igualdad y sin ningun tipo de discriminacion. h) Asegurar la gratuidad en todos los niveles y modalidades de los servicios educativos publicos de gestion estatal. i) Hacer efectivo el cumplimiento de la obligatoriedad escolar desde los cinco anos de edad en la Educacion Inicial hasta la finalizacion de la Educacion Secundaria. j) Desarrollar aptitudes, capacidades y competencias formativas, humanisticas, expresivas y creativas mediante la educacion cientifica, tecnologica, artistica, educacion fisica y ambiental. k) Resignificar la funcion de la escuela con estrategias pertinentes para promover la mejora de los procesos y los resultados de ensenanzas y aprendizajes con mayor autonomia y participacion de todos sus actores. l) Garantizar una formacion docente inicial de calidad y continua, con capacitacion y perfeccionamiento permanente para lograr la jerarquizacion de la profesion y especializacion en los diferentes niveles y modalidades, en el marco de una educacion inclusiva que atienda la diversidad. m) Garantizar la libertad de ensenanza, promoviendo una mayor complementacion y colaboracion entre las instituciones educativas de gestion estatal y las de gestion privada. n) Garantizar las condiciones laborales de los docentes, la infraestructura y el equipamiento de las escuelas. n) Brindar a las personas con discapacidad una propuesta pedagogica que les permita el pleno ejercicio de sus derechos, el desarrollo de sus posibilidades y su integracion. o) Desarrollar politicas de innovacion pedagogica, enfatizando las posibilidades que brinda la incorporacion de las tecnologias de informacion y comunicacion en el aula, y su uso en la planificacion, gestion y monitoreo del sistema educativo. p) Asegurar a las comunidades originarias el respeto a su lengua y a su identidad cultural, valorizando la multiculturalidad en la formacion de los alumnos y alumnas. q) Promover estrategias sistematicas de evaluacion integral de la calidad de los aprendizajes, que fortalezcan los circuitos de comunicacion y retroalimentacion para generar propuestas de mejoras ante las desigualdades. r) Coordinar acciones con organizaciones e instituciones deportivas y culturales para integrar la educacion formal con la no formal. s) Asegurar una formacion intelectual, corporal y motriz que favorezca el desarrollo intelectual, la practica de habitos de vida saludable, la prevencion de las adicciones, la formacion integral de una sexualidad responsable y la integracion reflexiva en los contextos socioculturales que habitan. t) Garantizar el derecho a una educacion artistica integral, para desarrollar capacidades interpretativas y creativas vinculadas a los distintos lenguajes y disciplinas contemporaneas. u) Promover y desarrollar experiencias educativas transformadoras, complementarias e innovadoras de la educacion comun, tendientes a mejorar la calidad educativa. v) Promover politicas que favorezcan la articulacion interinstitucional entre niveles del sistema educativo y con las universidades. w) Propiciar la participacion democratica de docentes y no docentes, familias, personal tecnico y profesional de apoyo, estudiantes, organizaciones de la sociedad civil en las instituciones educativas en todos los niveles y modalidades. x) Promover y respetar las formas asociativas de los alumnos y de los distintos actores de la comunidad educativa que tiendan a cumplir los objetivos de la politica educativa, en el marco del Proyecto Educativo Institucional. y) Formar y capacitar a los alumnos y docentes como lectores criticos y autonomos propiciando la creacion de bibliotecas escolares.


Documento: 14
Articulo: 326
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

El Sistema Educativo Provincial forma parte del Sistema Educativo Nacional y se integra por el conjunto de instituciones y acciones educativas regulados por el Estado tendientes a garantizar el pleno ejercicio del derecho constitucional de ensenar y aprender.


Documento: 14
Articulo: 327
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

El Sistema Educativo Provincial esta integrado por los establecimientos educativos de gestion estatal y privada, gestion cooperativa y gestion social, de los diferentes niveles y modalidades del sistema y la Universidad Autonoma de Entre Rios - U.A.D.E.R.- y sus instituciones educativas que se rigen por su ley de creacion y su Estatuto Academico y demas normas correspondientes.


Documento: 14
Articulo: 328
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

La obligatoriedad escolar se extiende desde el ultimo ano de Educacion Inicial hasta la finalizacion de la Educacion Secundaria. El Consejo General de Educacion garantizara su cumplimiento gradual a traves de alternativas institucionales pedagogicas y de promocion de derecho, en coordinacion con el Ministerio de Salud y Desarrollo Social, Consejo Provincial del Menor y el Poder Judicial.


Documento: 14
Articulo: 329
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

El Estado Provincial debera asegurar la obligatoriedad, mediante la organizacion de propuestas educativas "presenciales", "semi presenciales" o "a distancia" y la prestacion de servicios de educacion domiciliaria, hospitalaria y educacion en contextos de privacion de libertad, conforme con la reglamentacion que a tal efecto se establezca.


Documento: 14
Articulo: 330
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

El Estado Provincial asegura la educacion gratuita y laica en las instituciones de gestion estatal, en los diferentes niveles y modalidades del Sistema Educativo.


Documento: 14
Articulo: 331
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

El Sistema Educativo Provincial tiene una estructura unica en todo el territorio, con las siguientes caracteristicas: a) Presenta una estructura flexible, dinamica y coordinada que posibilita la articulacion horizontal y vertical de sus partes, garantizando la coherencia pedagogica entre niveles, ciclos y modalidades. b) Fortalece la vinculacion de la formacion tecnico profesional con el mundo del trabajo y el sistema productivo. c) Desarrolla una conciencia ambiental comprometida y critica que propenda en beneficio de las generaciones presentes y futuras. d) Fortalece la participacion democratica de los distintos actores de la comunidad educativa. e) Forma en valores de respeto a la dignidad humana, la convivencia pacifica entre los pueblos y el equilibrio ecologico. f) Incorpora los principios y valores del cooperativismo, del mutualismo y el asociativismo en los procesos de ensenanza aprendizaje y la capacitacion docente, en concordancia con los principios y valores establecidos en la Ley 16.583 y sus reglamentaciones. g) Promueve valores y actitudes que fortalezcan las capacidades de las personas para prevenir las adicciones y el uso indebido de las drogas. h) Promueve una educacion sexual escolar integral. i) Favorece una educacion artistica integral de calidad. j) Desarrolla las competencias necesarias para el manejo de los nuevos lenguajes y forma en el uso social, inteligente y productivo de las tecnologias de la comunicacion y la informacion.


Documento: 14
Articulo: 332
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

El Consejo General de Educacion establecera politicas y acciones educativas basadas en el uso de las tecnologias de la informacion y de la comunicacion y de los medios de comunicacion, a traves de la implementacion de alternativas educativas no convencionales que respondan a las particularidades de nuestra provincia.


Documento: 14
Articulo: 333
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO I: Integracion, obligatoriedad, gratuidad y caracteristicas

Las actividades pedagogicas estaran a cargo de personal docente titulado conforme lo establece la normativa vigente y se expediran titulos y certificados con validez nacional.


Documento: 14
Articulo: 334
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO II: Niveles del sistema educativo provincial

La estructura del Sistema Educativo Provincial esta integrada por cuatro (4) niveles: a) Educacion Inicial comprende el Jardin Maternal para ninos a partir de los 45 dias del nacimiento hasta los dos (2) anos de edad y el Jardin de Infantes, para los ninos desde los tres (3) y hasta los cinco (5) anos de edad, siendo este ultimo ano de caracter obligatorio. b) Educacion Primaria, a partir de los seis (6) anos de edad, de seis (6) anos de duracion, organizada en dos ciclos. c) Educacion Secundaria, de seis (6) anos de duracion, organizada en dos ciclos: el Ciclo Basico Comun y el Ciclo Orientado, de caracter diversificado segun areas del conocimiento. d) Educacion Superior, a partir de la finalizacion de la Educacion Secundaria, en el marco de la legislacion nacional vigente.


Documento: 14
Articulo: 358
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

La Educacion Superior comprende instituciones de Educacion Superior de gestion estatal o privada, sean de formacion docente, humanistica, social, tecnico profesional o artistica.


Documento: 14
Articulo: 359
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

La Educacion Superior se rige por la presente ley, las Leyes Nacionales No 26.058 de Educacion Tecnico Profesional y No 26.206 de Educacion Nacional, los Acuerdos Marco aprobados por el Consejo Federal de Educacion y normas nacionales que las sustituyan en el futuro.


Documento: 14
Articulo: 360
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

La Educacion Superior tiene como funciones basicas la produccion y socializacion de conocimientos, la formacion cientifica y profesional en las multiples dimensiones de la cultura provincial, regional y universal, la formacion y actualizacion disciplinaria y pedagogica para el ejercicio de la docencia en los niveles y modalidades del sistema educativo y la formacion de estudiantes en una trayectoria de profesionalizacion humanistica, social, tecnico-profesional y artistica, que posibilite su acceso al conocimiento y al campo laboral. Las instituciones de este nivel otorgan titulos de Educacion Superior.


Documento: 14
Articulo: 361
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

El Consejo General de Educacion planificara la distribucion territorial de los estudios superiores y tendra en cuenta el mapa de las carreras universitarias, las demandas y necesidades de cada region, a fin de optimizar los recursos y evitar la superposicion de propuestas educativas.


Documento: 14
Articulo: 362
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

Son objetivos de la Educacion Superior: a) Garantizar la calidad academica en los institutos de educacion superior. b) Generar conocimientos que propicien el desarrollo cientifico y tecnologico, asi como contenidos que expresen los valores de la cultura humana. c) Formar profesionales con excelencia academica y compromiso social. d) Propiciar la integracion de las instituciones que componen la Educacion Superior y de estas con los otros niveles y modalidades del sistema educativo provincial. e) Favorecer las vinculaciones con las universidades, centros de investigacion y produccion. f) Brindar propuestas diversificadas de servicios educativos para la formacion docente, tecnica, artistica, humanistica y social. g) Preparar para el ejercicio de la docencia en todos los niveles y modalidades del sistema educativo. h) Profundizar las instancias de participacion democratica de estudiantes, docentes y graduados. i) Propiciar mayor autonomia de gestion en las instituciones superiores. j) Propiciar instancias generadoras de formacion continua, tendientes al desarrollo profesional de los docentes en servicio; de investigacion y extension, para fortalecer la funcion social - educativa de los institutos.


Documento: 14
Articulo: 363
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

Los Disenos Curriculares del Nivel Superior estaran acordes con los Lineamientos aprobados en el Consejo Federal de Educacion para el reconocimiento de la validez nacional de los titulos por parte del Ministerio de Educacion de la Nacion.


Documento: 14
Articulo: 364
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

Los Institutos Superiores podran ofrecer Postitulos destinados a los docentes de los diferentes niveles y modalidades del sistema educativo con propuestas a termino. Se rigen por la normativa del Consejo Federal de Educacion y del Consejo General de Educacion.


Documento: 14
Articulo: 365
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

Para la creacion de nuevas carreras o cambios en las ya existentes, las instituciones, deberan efectuar un estudio de factibilidad que contenga aspectos vinculados a: potencial matricula, capacidad institucional, perfil de los recursos humanos, infraestructura y equipamiento, las demandas y necesidades de los distintos sectores locales y regionales.


Documento: 14
Articulo: 366
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

Las instituciones de Educacion Superior se articularan con las universidades, a traves de diferentes convenios especificos de investigacion, innovacion cientifica y tecnologica, de desarrollo profesional y de extension cultural o comunitaria, teniendo en cuenta los Acuerdos Marco firmados entre el Gobierno Provincial y las universidades.


Documento: 14
Articulo: 367
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

El gobierno de las instituciones de educacion superior es participativo y democratico, con la integracion prioritaria, de equipos directivos y organos con representacion de los distintos sectores que conforman la institucion.


Documento: 14
Articulo: 368
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

El ingreso a la docencia en el Nivel Superior es por Concurso, en el marco de la normativa vigente, exceptuando las designaciones en los institutos superiores de gestion privada que se regiran de acuerdo a lo prescripto por los Articulos 103o inc. e) y 132o de la presente Ley.


Documento: 14
Articulo: 369
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VI: Educacion superior

El ingreso de los estudiantes a las Instituciones de Educacion Superior, previa aprobacion de la educacion secundaria, sera directo, a traves de variadas instancias academicas que propongan las instituciones. En el caso de los ingresantes a carreras tecnico-profesionales podra exceptuarse a quienes no hayan culminado el nivel secundario previa evaluacion del perfil del mismo.


Documento: 14
Articulo: 370
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VII: Modalidades del sistema educativo provincial

Las modalidades del Sistema Educativo constituyen las opciones organizativas o curriculares de la educacion comun, dentro de uno o mas niveles del sistema educativo, que intentan dar respuesta a requerimientos especificos de formacion y atender particularidades de caracter permanentes o temporarios, personales o contextuales, con el proposito de garantizar la igualdad en el derecho a la educacion y cumplir con las exigencias legales, tecnicas y pedagogicas de los diferentes niveles educativos.-


Documento: 14
Articulo: 371
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO VII: Modalidades del sistema educativo provincial

Las modalidades del Sistema Educativo son ocho (8): la Educacion Tecnico Profesional; la Educacion Especial; la Educacion Permanente de Jovenes y Adultos; la Educacion Artistica; la Educacion Rural y de Islas, la Educacion Intercultural Bilingue; la Educacion en Contextos de Privacion de Libertad y la Educacion Domiciliaria y Hospitalaria.- 


Documento: 14
Articulo: 372
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO XIV: Educacion en contextos de privacion de libertad

La Educacion en Contextos de Privacion de Libertad es la modalidad que brinda la posibilidad a las personas que se encuentran privadas o restringidas de libertad, en establecimientos carcelarios o en instituciones de regimen cerrado como en otras situaciones que le impidan la asistencia a establecimientos educativos donde se dicte educacion obligatoria, que puedan acceder a propuestas educativas las que seran supervisadas por las autoridades del nivel o modalidad que corresponda.


Documento: 14
Articulo: 373
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO XIV: Educacion en contextos de privacion de libertad

Son objetivos de esta modalidad: a) Garantizar el cumplimiento de la escolaridad obligatoria a todas las personas privadas de libertad dentro de las instituciones de encierro o fuera de ellas cuando las condiciones de detencion lo permitan. b) Ofrecer formacion tecnico-profesional en todos los niveles y modalidades. c) Favorecer el acceso y permanencia en la Educacion Superior y un sistema gratuito de educacion a distancia. d) Asegurar alternativas de Educacion no-formal. e) Estimular la creacion artistica, la Educacion Fisica, la practica de deportes y la participacion de diferentes manifestaciones culturales.


Documento: 14
Articulo: 374
Capitulo: TITULO II: SISTEMA EDUCATIVO PROVINCIAL. CAPITULO XIV: Educacion en contextos de privacion de libertad

Los Disenos Curriculares y la organizacion institucional de Educacion Primaria y Secundaria, de Capacitacion Laboral y Formacion Profesional para jovenes y adultos en Contextos de Privacion de Libertad son flexibles, atienden la diversidad cultural, y presentan caracteristicas de educacion formal y no formal.


Documento: 14
Articulo: 375
Capitulo: TITULO III: EDUCACION DE GESTION PRIVADA

A los efectos de esta ley se entiende que la educacion de gestion privada tiene caracter publico por cuanto su objeto es la administracion de un bien publico y social y adquiere entidad sobre la base del reconocimiento de la libre eleccion de los padres.


Documento: 15
Articulo: 377
Capitulo: TITULO I: ESTRUCTURA Y FINES

La Universidad Autonoma de Entre Rios, es persona juridica, autonoma y autarquica, integrada por Facultades, Escuelas, Institutos, Departamentos, Niveles Educativos y otros organismos existentes o a crearse, y tiene su asiento en la ciudad de Parana.


Documento: 15
Articulo: 378
Capitulo: TITULO I: ESTRUCTURA Y FINES

Le corresponde a la Universidad: a) Elaborar, promover, desarrollar, transferir y difundir la cultura, la ciencia y la tecnologia, orientandolas de acuerdo a las necesidades nacionales, provinciales y regionales, pudiendo para ello interactuar con toda organizacion representativa de sus diversos sectores, a fin de informarse directamente sobre sus problemas e inquietudes y propender a la elevacion del nivel cultural de la colectividad para que le alcance el beneficio de los avances cientificos y tecnologicos y las elevadas expresiones de la cultura nacional e internacional. b) Impartir la ensenanza superior con caracter cientifico para la formacion de investigadores, profesionales y Tecnicos con amplia integracion cultural, capaces y conscientes de su responsabilidad social, debiendo estimular el intercambio de Docentes, Egresados y Estudiantes, con centros cientificos y culturales, nacionales y extranjeros. c) Ejercer junto con las demas universidades nacionales y provinciales la atribucion exclusiva e inalienable del Estado de otorgar los certificados habilitantes para el ejercicio profesional, expidiendo los titulos correspondientes a los estudios cursados en sus facultades. d) Desarrollar la creacion de conocimientos e impulsar los estudios sobre la realidad economica, demografica, cultural, social y politica del pais, adaptando aquellos a la solucion de los problemas provinciales, regionales y nacionales. e) Estar siempre abierta a toda expresion del saber y a toda corriente cultural e ideologica, sin discriminaciones, favoreciendo el desarrollo de la cultura nacional y contribuyendo al conocimiento reciproco entre los pueblos. f) Propender a la coordinacion de los ciclos de ensenanza en la unidad del proceso educativo, tendiendo a la obtencion de una gradacion logica del conocimiento en cuanto al contenido, intensidad y profundidad. g) Coordinar con las demas universidades nacionales y provinciales el desarrollo de los estudios superiores y de investigacion. h) Asegurar a sus miembros los servicios sociales que permitan las mejores condiciones tendientes al efectivo aprovechamiento de sus beneficios, velando por la calidad de vida, la proteccion de la salud y adecuada remuneracion a su personal segun la funcion desempenada. i) Requerir a los integrantes de los Cuerpos Universitarios la participacion en toda tarea de extension universitaria. j) Mantener la necesaria vinculacion con los Egresados, tendiendo a su perfeccionamiento, organizando toda actividad conducente a ese objetivo. k) Preservar y educar en el espiritu de la moral y etica publica, en el respeto y defensa de los derechos humanos, de las libertades democraticas, de la soberania e independencia de la Nacion, contribuyendo a la confraternidad humana y a la paz entre los pueblos y propendiendo a que sus conocimientos sean colocados a su servicio, para el mejoramiento del nivel de vida en el marco del desarrollo provincial, regional y nacional. l) Proclamar y garantizar la mas amplia libertad de juicios y criterios, doctrinas y orientaciones filosoficas en el dictado de la catedra universitaria.


Documento: 15
Articulo: 379
Capitulo: TITULO I: ESTRUCTURA Y FINES

Participan en la vida universitaria todas las personas que posean ciudadania en las categorias de Profesor Universitario, Graduado, Estudiante y Administrativo. Los Titulares de ciudadania de una misma categoria constituyen un Cuerpo Universitario. No se podra simultaneamente, pertenecer a mas de uno de ellos. Los derechos y obligaciones, asi como el otorgamiento, ejercicio y cancelacion de la "Ciudadania Universitaria", son materia de reglamentacion que dictara el Consejo Superior.


Documento: 15
Articulo: 380
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad

El gobierno de la Universidad coordina la labor de los organismos que la integran.


Documento: 15
Articulo: 381
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad

Son organos del gobierno universitario: a) La Asamblea Universitaria. b) El Consejo Superior. c) El Rector.


Documento: 15
Articulo: 382
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION A: De la Asamblea Universitaria

La Asamblea Universitaria es el organo superior de la Universidad. Se constituye con todos los miembros del Consejo Superior y de los Consejos Directivos de las Facultades. Debe reunirse, por lo menos, una vez al ano.


Documento: 15
Articulo: 383
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION A: De la Asamblea Universitaria

El Rector o su reemplazante, es el presidente de la Asamblea Universitaria. Todos los integrantes tienen voz y voto en las deliberaciones, excepcion hecha del Presidente que solo decide en caso de segundo empate.


Documento: 15
Articulo: 384
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION A: De la Asamblea Universitaria

La convocatoria a la Asamblea Universitaria sera realizada por el Rector o su reemplazante, previa decision del Consejo Superior o a peticion de un tercio de los miembros de aquella o de la mitad mas uno de los Consejos Directivos, quedando la misma sujeta a la aprobacion del Consejo Superior. En todos los casos la convocatoria debe expresar el objeto de la misma y hacerse con quince dias de anticipacion como minimo. El quorum de la Asamblea Especial para dar cumplimiento al Articulo 9 inciso c) debera ser de las tres cuarta partes de los integrantes del Cuerpo.


Documento: 15
Articulo: 385
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION A: De la Asamblea Universitaria

La Asamblea Universitaria tiene las siguientes atribuciones: a) Fijar la politica universitaria. b) Dictar o modificar el Estatuto. c) Elegir Rector y Vicerrector por mayoria absoluta del total de los miembros presentes. d) Decidir sobre la renuncia del Rector y Vicerrector. e) Suspender o remover por causas justificadas al Rector y al Vicerrector. f) Dictar su reglamento interno. g) Tomar a su cargo el gobierno de la Universidad, designando a quienes deben ejercerlo, en caso de falta de funcionamiento del Consejo Superior por imposibilidad efectiva del quorum. h) Crear nuevas Facultades, Escuelas, Institutos, Departamentos y Niveles Educativos o suprimir las existentes, por mayoria absoluta del total de sus miembros. i) Tratar la memoria anual presentada por el Consejo Superior, aprobando o rechazando la misma. j) Ejercer todo acto de jurisdiccion superior no prescripto en este Estatuto. Ninguna decision de la Asamblea Universitaria puede modificarse durante el transcurso del ano en el que es adoptada, salyo que lo sea por las dos terceras partes de los miembros que integran el Cuerpo.


Documento: 15
Articulo: 386
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION B: Del Consejo Superior

El Consejo Superior esta integrado por el Rector, los Decanos en representacion de las Facultades, un Consejero Profesor Titular y/o Asociado por cada Facultad; tres Consejeros Profesores Titulares y/o Asociados; dos Consejeros Profesores Adjuntos, dos Consejeros Profesores Jefe de Trabajos Practicos y/o Auxiliar Docente, cuatro Consejeros Graduados; seis Consejeros Estudiantes y dos Consejeros Administrativos. El Rector o su reemplazante es el presidente del organo y todos sus integrantes tienen voz y voto, excepcion hecha de quien preside, que solo decidira en caso de segundo empate. En caso de incorporarse Consejeros Profesores por creacion de nuevas Facultades, se incrementara el numero de representantes de los demas Cuerpos, debiendo mantenerse el cincuenta por ciento de la representacion del claustro Docente.


Documento: 15
Articulo: 387
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION B: Del Consejo Superior

El Consejo Superior se reune por convocatoria del Rector, de su reemplazante o a pedido de un tercio de los integrantes del Cuerpo. En ausencia del Rector y su reemplazante, la convocatoria sera decidida por la mayoria de los Decanos y en su defecto, por voluntad de la mitad mas uno de los integrantes del Cuerpo.


Documento: 15
Articulo: 388
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION B: Del Consejo Superior

El reemplazo del Rector y de los Decanos sera procedente por razones circunstanciales o accidentales, previa delegacion del cargo a quien corresponda. Los Consejeros Profesores, Graduados, Estudiantes y Administrativo, solo pueden ser reemplazados en caso de vacancia de sus cargos o cuando se acuerde a los Titulares licencia no inferior a dos meses. En tales casos la incorporacion y el cese del suplente se produce automaticamente por la iniciacion y el fenecimiento del termino que corresponda a la licencia acordada al Titular, quien se reintegra, tambien, en forma automatica. En su defecto, se reputara vacante el cargo, debiendo continuar el reemplazante hasta la terminacion del periodo que senala el Articulo 13.


Documento: 15
Articulo: 389
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION B: Del Consejo Superior

Los Consejeros integrantes del Consejo Superior duran en sus funciones: a) Los Consejeros Profesores, cuatro anos. b) Los Consejeros Graduados dos anos. c) Los Consejeros Estudiantes un ano. d) Los Consejeros Administrativos cuatro anos.


Documento: 15
Articulo: 390
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION B: Del Consejo Superior

El Consejo Superior tiene las siguientes atribuciones: a) Ejercer la direccion de la Universidad en cumplimiento del programa trazado por la Asamblea Universitaria y de los fines del presente Estatuto. b) Intervenir las Facultades a requerimiento de sus autoridades o por hallarse subvertidos los principios que informan el presente Estatuto. En este ultimo caso se requeriran los dos tercios de votos de los miembros presentes. c) Crear Institutos de investigacion, Departamentos y secciones, y fomentar la labor cientifica, cultural y artistica que desarrollan sus organismos. d) Fomentar la extension universitaria, la transferencia cientifico-tecnologica, el desarrollo cultural y el bienestar universitario. e) Promover la creacion de nuevas Facultades, Institutos, Escuelas y Niveles Educativos. f) Crear o transformar las carreras, fijar los alcances de los titulos universitarios y modificar la estructura de las Facultades, con informe de las mismas. g) Aprobar las ordenanzas de revalida y habilitacion de titulos extranjeros proyectadas por las Facultades. h) Nombrar los Docentes universitarios, a propuesta de los Consejos Directivos de las Facultades, conforme el Articulo 23, inciso f). i) Otorgar el titulo de Doctor Honoris Causa. j) Decidir en ultima instancia en las cuestiones contenciosas que haya resuelto el Rector o las Facultades, con excepcion de los casos expresamente reservados a estas. k) Proponer reformas al Estatuto, las que debe someter a consideracion de la Asamblea Universitaria. l) Aprobar la memoria anual, elaborada por el Rector y someterla a consideracion de la Asamblea Universitaria. m) Dictar su reglamento interno y las disposiciones necesarias para el regimen comun de los estudios y gestiones. n) Fijar las normas que correspondan para racionalizar la actividad administrativa. o) Reglamentar el otorgamiento, ejercicio y cancelacion de la ciudadania universitaria. p) Formular el presupuesto anual de la Universidad. q) Aprobar o rechazar las cuentas de inversion que anualmente debe presentar el Rector. r) Reglamentar la adquisicion, venta, permuta y constitucion de gravamenes de los bienes de la Universidad. s) Aceptar herencias, legados y donaciones que se hicieran a la Universidad o a sus Facultades, Institutos, Departamentos y Niveles Educativos. t) Aprobar las ordenanzas de concursos para Profesores. u) Aprobar los planes de estudios proyectados por las Facultades.


Documento: 15
Articulo: 391
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION C: Del Rector

El Rector es el representante de la Universidad y dirige todas las actividades de la misma. Dura cuatro anos en sus funciones y podra ser reelecto una sola vez en forma consecutiva. Para ser designado se requiere ser ciudadano argentino, poseer grado universitario, haber cumplido treinta anos de edad y ser o haber sido Profesor por concurso de una Universidad Nacional o Provincial.


Documento: 15
Articulo: 392
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION C: Del Rector

El rector tiene a su cargo las siguientes funciones: a) Cumplir y hacer cumplir las resoluciones o acuerdos de la Asamblea Universitaria y del Consejo Superior. b) Realizar, con la colaboracion de los Decanos, la obra de coordinacion y desarrollo programada por la Asamblea Universitaria y el Consejo Superior. c) Mantener relaciones con las corporaciones e instituciones cientificas y universitarias del pais y del extranjero. d) Convocar y presidir las reuniones de la Asamblea Universitaria y del Consejo Superior, sin perjuicio de las otras disposiciones sobre el particular. En ausencia o por impedimento del Rector y Vicerrector, la convocatoria a reunion del Consejo Superior se realizara por decision de la mayoria de los Decanos. En caso de que estos no convoquen a reunion dentro de los treinta dias, la convocatoria podra efectuarse por decision de la mitad mas uno de los integrantes del Cuerpo. e) Preparar la memoria anual y el informe sobre necesidades, sometiendolos a consideracion del Consejo Superior. f) Suscribir conjuntamente con los Decanos los diplomas de doctor, los titulos profesionales universitarios y las constancias de revalidas y habilitaciones. Asimismo, juntamente con el Director del organismo respectivo, los diplomas que expiden Institutos Superiores de ensenanza, en razon de los estudios de caracter universitario que se impartan en ellos. g) Pedir reconsideracion, en la sesion siguiente o en sesion extraordinaria, de toda resolucion del Consejo Superior que considere inconveniente para la buena marcha de la Universidad, pudiendo suspender entre tanto su ejecucion. h) Disponer los pagos que deben realizarse con los fondos votados en el presupuesto de la Universidad y los demas que el Consejo Superior autorice. i) Adoptar todas las providencias necesarias para la buena marcha de la Universidad. j) Rendir cuenta de su administracion al Consejo Superior. k) Designar y remover al personal de la Universidad, cuyo nombramiento no sea facultativo del Consejo Superior, de acuerdo a las normas reglamentarias correspondientes.


Documento: 15
Articulo: 393
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 1: De la Universidad. SECCION C: Del Rector

Mediando enfermedad o ausencia por mas de diez dias, el Rector delegara el ejercicio de sus funciones en el Vicerrector, quien lo sustituye, ademas, en caso de renuncia, inhabilidad o ausencia definitiva. En los mismos casos previstos, y en ausencia del Vicerrector, desempena sus funciones el Decano que el Consejo Superior designe. En casos de vacancia del Rector y Vicerrector, debera convocarse a la Asamblea Universitaria para que proceda a la eleccion de nuevo Rector.


Documento: 15
Articulo: 394
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades

Las Facultades desarrollan la labor universitaria especialidades, con independencia tecnica y Docente.


Documento: 15
Articulo: 395
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades

Son organos del gobierno de las Facultades: a) Los Consejos Directivos. b) Los Decanos.


Documento: 15
Articulo: 396
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION A: De los Consejos Directivos

El Consejo Directivo de cada Facultad esta integrado por el Decano, cuatro Consejeros Profesores Titulares y/o Asociados, tres Consejeros Profesores Adjuntos, dos Consejeros Docentes Jefe de Trabajo Practico y/o Auxiliares Docentes; tres Consejeros Graduados, cinco Consejeros Estudiantes y un Consejero Administrativo. El Decano preside el Cuerpo y solo tendra voto en caso de empate.


Documento: 15
Articulo: 397
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION A: De los Consejos Directivos

La designacion de los integrantes del Consejo Directivo se hace por iguales terminos a los establecidos en el Articulo 13 y su reemplazo se ajustara a las normas previstas en el Articulo 12.


Documento: 15
Articulo: 398
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION A: De los Consejos Directivos

Cuando de la Facultad dependa una Escuela Universitaria el Director de la misma tendra voz en el Consejo Directivo. Cada Escuela Universitaria tendra una comision asesora Docente.


Documento: 15
Articulo: 399
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION A: De los Consejos Directivos

El Consejo Directivo tiene las siguientes funciones: a) Coordinar y ampliar la obra de las Escuelas, Departamentos, Institutos, Catedras y demas Organismos cientificos, Tecnicos, culturales y Docentes que forman la Facultad. b) Proyectar planes de estudio. Aprobar, reformar o rechazar los programas de ensenanza proyectados por los Profesores o Departamentos. c) Reglamentar la docencia libre y la catedra paralela. d) Reglamentar los cursos intensivos. e) Expedir certificados en virtud de los cuales hayan de otorgarse los diplomas universitarios y los de revalida y habilitacion expedidos por universidades extranjeras. f) Proponer al Consejo Superior el nombramiento de sus Docentes universitarios. g) Elegir al Decano y al Vicedecano de acuerdo a lo dispuesto en los Articulos 34 y 35. h) Designar a sus Docentes Interinos. i) Dictar el reglamento interno y demas normas necesarias que no esten reservadas al Consejo Superior. j) Elaborar y elevar al Consejo Superior el presupuesto anual. k) Rendir cuentas al Consejo Superior de la inversion de fondos. i) Proyectar nuevas fuentes de ingresos para la Facultad o Institutos. m) Aprobar el calendario academico. n) Promover acciones de docencia, investigacion y extension.


Documento: 15
Articulo: 400
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION B: De los Decanos

El decano es el representante de la Facultad y dirige todas las actividades de la misma. Para ser Decano se requiere ser ciudadano argentino, haber cumplido treinta anos de edad, poseer grado universitario, ser Docente Titular y/o Asociado de la Facultad designado conforme el Articulo 56, inciso a) de este Estatuto. El Decano durara cuatro anos en el cargo y podra ser reelecto una sola vez en forma consecutiva.


Documento: 15
Articulo: 401
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION B: De los Decanos

El Decano tiene a su cargo las siguientes funciones: a) Organizar y dirigir la obra de coordinacion Docente, cientifica y cultural de la Facultad. b) Convocar y presidir las sesiones del Consejo Directivo. c) Cumplir y hacer cumplir las resoluciones de los organos del gobierno universitario y del Consejo Directivo. d) Elevar anualmente al Consejo Superior una memoria relativa a la marcha de la Facultad y un informe acerca de sus necesidades. e) Nombrar y separar, de acuerdo a las normas pertinentes, a los empleados cuyo nombramiento y remocion no corresponda al Consejo Directivo. f) Proponer al Consejo Directivo la designacion de Docentes Interinos de acuerdo con la reglamentacion pertinente. g) Elaborar el calendario academico. h) Disponer los pagos de los fondos asignados en las partidas de presupuesto y de aquellos especiales autorizados por el Consejo Directivo. i) Disponer las medidas necesarias para el mejor funcionamiento Administrativo de la Facultad. j) Rendir cuenta de su gestion al Consejo Directivo. k) Pedir reconsideracion en la sesion siguiente o en sesion extraordinaria, de toda resolucion del Consejo Directivo que considere inconveniente para la buena marcha de la Facultad, pudiendo suspender, entre tanto su ejecucion.


Documento: 15
Articulo: 402
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION B: De los Decanos

En casos de enfermedad o ausencia por mas de diez dias, el Decano delegara sus funciones en el Vicedecano, quien lo sustituira, mediando renuncia, inhabilidad o ausencia definitiva. En ausencia del Vicedecano ejercera sus funciones el Consejero Profesor Titular y/o asociado que el Consejo Directivo designe. En casos de vacancia del Decano y Vicedecano, debera convocarse al Consejo Directivo para que proceda a la eleccion de nuevo Decano.


Documento: 15
Articulo: 403
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION C: De las Escuelas Universitarias

Las Escuelas Universitarias constituiran Comisiones Asesoras Docentes, respetando las proporciones del Articulo 20. El Consejo Directivo aprobara la reglamentacion relativa a sus atribuciones y funcionamiento.


Documento: 15
Articulo: 404
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION C: De las Escuelas Universitarias

Los Directores de estas Escuelas seran nombrados por el Consejo Directivo de la Facultad a propuesta de la Comision Asesora Docente, en la forma y condiciones que determine el reglamento.


Documento: 15
Articulo: 405
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION D: De los Niveles Educativos

Los establecimientos de ensenanza de distintos Niveles Educativos que dependan de las Facultades funcionaran conforme al reglamento que dicten estas ultimas, con aprobacion del Consejo Directivo. La supervision de los mismos corresponde al Consejo Directivo y al Decano de la Facultad, quedando la direccion inmediata a cargo del Director de dichos establecimientos.


Documento: 15
Articulo: 406
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION D: De los Niveles Educativos

El Director y Vicedirector de los establecimientos de distintos Niveles Educativos seran nombrados por el Consejo Directivo de la Facultad entre los Profesores Titulares designados por concurso.


Documento: 15
Articulo: 407
Capitulo: TITULO II: ORGANOS Y FUNCIONES. CAPITULO 2: De las Facultades. SECCION D: De los Niveles Educativos

Los Profesores de los Niveles Educativos seran nombrados por los Consejos Directivos de las Facultades, previo concurso y de acuerdo con las disposiciones prescriptas para la provision de las catedras universitarias. Los reglamentos de estudio, de organizacion y disciplina para estos establecimientos, deberan ser proyectados por una "Comision Especial", de la que formaran parte el director del mismo, dos representantes de los Profesores, un representante de los alumnos pertenecientes al ultimo ano, y un representante de los Egresados del propio establecimiento y sometidos a la aprobacion del Consejo Directivo.


Documento: 15
Articulo: 408
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 1: De la designacion de Rector y Vicerrector

La eleccion de Rector y Vicerrector se hara en sesion especial de la Asamblea Universitaria, por mayoria absoluta de votos de los integrantes de la misma.


Documento: 15
Articulo: 409
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 1: De la designacion de Rector y Vicerrector

Si ningun candidato alcanzare tal mayoria absoluta de votos en la primera votacion, la misma se repetira, y si tampoco la obtiene esta vez, la tercera votacion se concretara a los dos candidatos que hubieren reunido mayor numero de votos en el computo anterior, resultando electo el candidato mas votado, cualquiera sea el numero obtenido. En caso de empate se decidira por sorteo y la Asamblea Universitaria no podra levantarse sino despues de elegido el Rector y el Vicerrector.


Documento: 15
Articulo: 410
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 2: De la designacion de los Decanos y Vicedecanos

El Decano y el Vicedecano seran elegidos por el Consejo Directivo en sesion especial, por mayoria absoluta de votos de los integrantes del mismo.


Documento: 15
Articulo: 411
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 2: De la designacion de los Decanos y Vicedecanos

Si ningun candidato alcanzare tal mayoria absoluta de votos en la primera votacion, la misma se repetira, y si tampoco obtiene esta vez, la tercera votacion se concretara a los dos candidatos que hubieren reunido mayor numero de votos en el computo anterior, resultando electo el candidato mas votado, cualquiera sea el numero obtenido. En caso de empate se decidira por sorteo y la sesion del Consejo Directivo no podra levantarse sino despues de elegido el Decano y el Vicedecano.


Documento: 15
Articulo: 412
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 3: De la eleccion de Consejeros Profesores

Los Profesores Titulares y/o asociados, adjuntos y jefes de trabajos practicos y/o Auxiliares Docentes inscriptos en padrones separados, votaran por sus respectivos candidatos a Consejeros ante el Consejo Directivo.


Documento: 15
Articulo: 413
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 3: De la eleccion de Consejeros Profesores

La eleccion se hara mediante boletas que depositaran personalmente en urnas distintas y la distribucion de los cargos se realizara por el sistema de representacion proporcional D Hont.


Documento: 15
Articulo: 414
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 3: De la eleccion de Consejeros Profesores

Por el mismo procedimiento del Articulo 37 la totalidad de los Profesores electores procederan a la eleccion del Consejero Profesor y su suplente ante el Consejo Superior, debiendo pertenecer al padron de Titulares y/o asociados. Las designaciones se haran a simple pluralidad de sufragios, y en caso de empate, por sorteo.


Documento: 15
Articulo: 415
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 3: De la eleccion de Consejeros Profesores

En reunion especial, convocada al efecto por el Rector, y bajo su presidencia, los Consejeros Profesores Titulares y/o asociados, adjuntos y jefe de trabajos practicos y/o Auxiliares Docentes se constituiran en Colegio Electoral de acuerdo a sus respectivas categorias, para la eleccion de los consejeros Titulares y Suplentes ante el Consejo Superior. Para el funcionamiento del Colegio Electoral, se aplicaran las disposiciones contenidas en los incisos a), b), c), d) y e) del Articulo 42.


Documento: 15
Articulo: 416
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 4: De la eleccion de Consejeros Graduados

Para la eleccion de Consejeros Graduados ante el Consejo Directivo de cada Facultad, la misma confeccionara el padron y la eleccion se hara en forma directa con listas oficializadas. En este Cuerpo el sufragio podra emitirse por correspondencia.


Documento: 15
Articulo: 417
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 4: De la eleccion de Consejeros Graduados

Oficializandose mas de una lista, se designaran dos Consejeros por la mayoria y uno por la minoria. En caso de que la minoria mas votada no obtenga por lo menos el 25% de los votos de la mayoria, se adjudicara a esta ultima el respectivo cargo. El voto sera secreto y en caso de empate se resolvera por sorteo.


Documento: 15
Articulo: 418
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 4: De la eleccion de Consejeros Graduados

En reunion especial, convocada al efecto por el Rector, y bajo su presidencia, los Consejeros como asi tambien los Estudiantes electos por la mayoria y minoria ante los respectivos Consejos Directivos, se constituiran, separadamente, en Colegios Electorales, procediendo a elegir sus representantes ante el Consejo Superior, por el sistema de representacion proporcional y en la siguiente forma: a) El numero total de Consejeros electos ante los Consejos Directivos se dividira por el numero de cargos a cubrir y el resultado asi obtenido constituira el cociente aplicable para la adjudicacion de las bancas. b) La minoria que no alcanzare el cociente resultante no tendra representacion. c) Si quedara algun cargo a cubrir, este correspondera a la representacion que tenga mayor residuo. d) Para el funcionamiento del Colegio Electoral se requiere la presencia de la mitad mas uno de los miembros. e) En caso de no lograr quorum en anteriores citaciones, en la tercera de ellas el Colegio Electoral se constituira con la presencia de los Consejeros que asistan.


Documento: 15
Articulo: 419
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 5: De la eleccion de Consejeros Estudiantes

Para la eleccion de Consejeros Estudiantes ante el Consejo Directivo de cada Facultad, la misma confeccionara el padron y la eleccion se hara en forma directa con listas oficializadas.


Documento: 15
Articulo: 420
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 5: De la eleccion de Consejeros Estudiantes

Oficializandose mas de una lista, se designaran tres consejeros por la mayoria y dos consejeros por la minoria. En caso de que la minoria mas votada no obtenga por lo menos el 25% de los votos de la mayoria, se adjudicara a esta ultima el respectivo cargo. El voto sera secreto y en caso de empate se resolvera por sorteo.


Documento: 15
Articulo: 421
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 5: De la eleccion de Consejeros Estudiantes

Para la eleccion de los Consejeros Estudiantes ante el Consejo Superior se aplicaran las disposiciones del Articulo 42.


Documento: 15
Articulo: 422
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 6: De la eleccion de Consejeros Administrativos

Para la eleccion de representantes Administrativos ante el Consejo Directivo de cada Facultad, la misma confeccionara el padron y la eleccion se hara en forma directa con listas oficializadas, resultando electo el candidato por simple mayoria.


Documento: 15
Articulo: 423
Capitulo: TITULO III: REGIMEN ELECTORAL. CAPITULO 6: De la eleccion de Consejeros Administrativos

La eleccion de los Consejeros Administrativos ante el Consejo Superior se efectuara en forma directa y en padron unico de toda la Universidad. Oficializandose mas de una lista, se designara por el sistema de simple mayoria, un Consejero Titular y un suplente por la mayoria y un Titular y un suplente por la minoria. En caso de que la minoria mas votada no obtenga por lo menos el treinta por ciento de los votos, se adjudicara esta ultima a la mayoria. El voto sera secreto y en caso de empate se resolvera por sorteo.


Documento: 15
Articulo: 424
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

El Cuerpo de Docentes Universitarios esta integrado por los Profesores: Titulares, Asociados, Adjuntos, Jefes de Trabajos Practicos y Auxiliares Docentes en ejercicio de sus funciones y de la ciudadania universitaria.


Documento: 15
Articulo: 425
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Sera objeto del Cuerpo de Docentes Universitarios propender al cumplimiento de los fines del presente Estatuto y a la defensa de los intereses de sus integrantes.


Documento: 15
Articulo: 426
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los integrantes del Cuerpo son electores de consejeros y elegibles como tales en la categoria correspondiente.


Documento: 15
Articulo: 427
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

El Cuerpo de Docentes Universitarios asesoraran a solicitud del Consejo Directivo sobre: a) Orientacion y correlacion de la ensenanza. b) Proyecto y reforma de planes de estudio. c) Creacion de nuevos Organismos en la Facultad.


Documento: 15
Articulo: 428
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Decanos podran convocar al Cuerpo a los fines precedentes, cuando lo estime pertinente, sin perjuicio de que la convocatoria pueda efectuarse por la tercera parte de sus miembros.


Documento: 15
Articulo: 429
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

En la formacion del Cuerpo Docente, la Universidad asume los compromisos de vincular procesos institucionales de formacion, perfeccionamiento, actualizacion y un sistema de remuneracion adecuada a posibilitar el ejercicio de la catedra, con dedicacion exclusiva.


Documento: 15
Articulo: 430
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

La Universidad garantizara la actualizacion y perfeccionamiento de sus Docentes mediante la asistencia a cursos o actividades equivalentes. Dicho perfeccionamiento no se limitara a la capacitacion en el area cientifica o profesional especifica y en los aspectos pedagogicos, sino que incluira tambien, el desarrollo de una adecuada formacion interdisciplinaria. Se alentara el intercambio de personal Docente con otras universidades.


Documento: 15
Articulo: 431
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Todos los Profesores concursados, si poseen ocho anos de antiguedad en tal situacion, podran gozar de un ano de licencia con goce de haberes para realizar actividades academicas y de perfeccionamiento segun plan de trabajo aprobado por la autoridad correspondiente y de acuerdo con la Reglamentacion que dicte el Consejo Superior.


Documento: 15
Articulo: 432
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

La Universidad contara con las siguientes categorias de Docentes universitarios, designados por el Consejo Superior, a propuesta de la respectiva Facultad; a) Profesores: Titulares, Asociados, Adjuntos, Jefes de Trabajos Practicos y Auxiliares Docentes designados por concurso abierto de antecedentes y prueba de oposicion. b) Profesores Universitarios Honorarios designados sin concurso ni prueba de oposicion. c) Docentes contratados o Interinos. Docentes Auxiliares alumnos.


Documento: 15
Articulo: 433
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Profesores Titulares y Asociados tendran las siguientes funciones y obligaciones: a) Dirigir e impartir la ensenanza de su asignatura, de acuerdo a los planes y normas fijados por la respectiva Facultad. b) Establecer el plan de distribucion de la ensenanza que le corresponda con los Profesores Adjuntos, de acuerdo con la reglamentacion de la Facultad. c) Proyectar los programas de sus catedras. d) Dar conferencias o cursos intensivos en el local de la Facultad. e) Colaborar en las publicaciones e investigaciones de los Institutos Cientificos de la Universidad y de las Facultades. f) Cumplir los horarios de examenes que les fije la Facultad. g) Desempenar las comisiones cientificas, Docentes, universitarias y culturales que le encomiende la Universidad o Facultad. h) Desarrollar acciones pertinentes de formacion academica del equipo de catedra.


Documento: 15
Articulo: 434
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Profesores Adjuntos tendran las siguientes funciones y obligaciones: a) Colaborar con el Titular en la ensenanza de su catedra. b) Reemplazar temporariamente al Titular en caso de ausencia o vacancia. c) Desempenar las mismas tareas establecidas para los Titulares en los incisos d), e) f) g) y h) del Articulo anterior, asi como las otras funciones que especificamente reglamente cada Facultad.


Documento: 15
Articulo: 435
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Jefes de Trabajos Practicos y Profesores Auxiliares Docentes son aquellos Docentes que tienen como mision preparar, conducir y evaluar la aplicacion practica de los contenidos de la ensenanza, segun la planificacion de la catedra. A tales fines tendran las siguientes funciones y obligaciones: a) Asistir a los Profesores en el dictado de clases que se consideren convenientes para lograr la optimizacion de los procesos de ensenanza y aprendizaje. b) Participar en las tareas de investigacion y extension que de acuerdo al planeamiento de catedra o Departamento, le determine el Profesor responsable. c) Tender a su propia especializacion dentro de la planificacion institucional de perfeccionamiento de los recursos humanos. d) Cualquier otra actividad que dentro del planeamiento de catedra, el Profesor responsable considere pertinente.


Documento: 15
Articulo: 436
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Profesores Auxiliares Docentes y Docentes Auxiliares alumnos tienen como mision colaborar con los Profesores y Jefes de Trabajos Practicos en la preparacion, conduccion y evaluacion de la aplicacion practica de los contenidos de la ensenanza. A tales fines tendran las siguientes funciones y obligaciones: a) Participar en las tareas de investigacion y extension que de acuerdo al planeamiento de catedra o Departamento, le determine el Profesor. b) Tender a su propia especializacion dentro de la planificacion institucional de perfeccionamiento de los recursos humanos. c) Cualquier otra actividad que dentro del planeamiento de catedra el Profesor responsable considere pertinente.


Documento: 15
Articulo: 437
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

La designacion de Profesores sera por periodo limitado de ocho anos. El Profesor en funcion de Rector y/o Decano mantiene su condicion mientras dure su mandato y por un periodo igual al del cargo desempenado con un maximo de cuatro anos.


Documento: 15
Articulo: 438
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Vencido el plazo de la designacion originada en el concurso, el Docente Universitario tendra derecho, sobre la base de la evaluacion que al efecto se realice, que le sea renovada su designacion en la misma categoria de revista y con los alcances previstos en el Articulo 61, por otro periodo, y asi sucesivamente. Si no le fuera renovada la designacion se llamara a concurso segun el Articulo 14, inciso t).


Documento: 15
Articulo: 439
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Las propuestas al Consejo Superior para la designacion de Docentes honorarios, requiere los dos tercios de los integrantes del Consejo Directivo.


Documento: 15
Articulo: 440
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

El Profesor que se retira de la ensenanza podra recibir, en los casos de destacada actuacion cientifica o Docente, el titulo de Profesor honorario, con caracter vitalicio, de acuerdo a lo previsto en el Articulo 56, inciso b).


Documento: 15
Articulo: 441
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Docentes contratados desempenaran las tareas que les asigne el contrato respectivo.


Documento: 15
Articulo: 442
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Los Consejos Directivos podran, cuando ello sea imprescindible, designar temporariamente Docentes Interinos y mientras se sustancie el correspondiente concurso.


Documento: 15
Articulo: 443
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION A: De los Docentes Universitarios

Cada Facultad dictara la ordenanza respectiva para la provision de los cargos de Docentes Interinos, con aprobacion del Consejo Superior, debiendo ajustarse a las normas del presente Estatuto y a las ordenanzas correspondientes a los concursos de Profesores.


Documento: 15
Articulo: 444
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION B: De los Graduados

Sera objeto del Cuerpo de Graduados propender al cumplimiento de los fines del presente Estatuto.


Documento: 15
Articulo: 445
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION B: De los Graduados

El Cuerpo de Graduados se integra con los Egresados de esta Universidad, cualquiera sea su lugar de residencia y con los de cualquier Universidad Nacional que resida en la provincia de Entre Rios. La inscripcion en el padron pertinente correspondera a peticion del interesado, atendiendo a la especialidad por Facultades en tanto se halle en ejercicio de la ciudadania respectiva. En ningun caso podra integrar el padron de Graduados en la Universidad Autonoma de Entre Rios quien figure inscripto en otro similar del pais o integre otro claustro y ejerza los derechos que como tal le correspondan.


Documento: 15
Articulo: 446
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION B: De los Graduados

Para ser elector graduado, la inscripcion en los padrones debera tener, como minimo una antiguedad de seis meses.


Documento: 15
Articulo: 447
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION B: De los Graduados

Para ser Consejeros Graduados ante el Consejo Superior y ante los Consejos Directivos, se requiere una antiguedad minima de dos anos en los respectivos registros.


Documento: 15
Articulo: 448
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

Sera funcion principal del Cuerpo de Estudiantes propender al cumplimiento de los fines que enuncia el presente Estatuto y a la defensa de los intereses de sus integrantes.


Documento: 15
Articulo: 449
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

El Cuerpo de Estudiantes se integra con los inscriptos de cada Facultad, en las categorias que se establece en el Articulo 75 y en ejercicio de la ciudadania universitaria. No ejercen la ciudadania los alumnos que cursan carreras con modalidad a distancia.


Documento: 15
Articulo: 450
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

El Cuerpo de Estudiantes, como parte integrante de la Universidad, se dara sus propias normas y reglamentara su funcionamiento, asegurando la participacion de todos los sectores de opinion.


Documento: 15
Articulo: 451
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes



La Universidad reconocera las siguientes categorias de Estudiantes: a) Regular. b) Libre. c) Vocacional. Cada Facultad reglamentara estas categorias.


Documento: 15
Articulo: 452
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

Para ser Consejero Estudiante se requiere haber aprobado por lo menos la mitad de las asignaturas de una tecnicatura y un tercio de una carrera de grado en la que esta inscripto y reunir la condicion de elector.


Documento: 15
Articulo: 453
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

El Cuerpo de Estudiantes elegira anualmente, en un solo comicio, sus Consejeros Titulares y Suplentes a los Consejos Directivos que actuaran como representantes de aquel.


Documento: 15
Articulo: 454
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

La Universidad prestara preferente atencion al desarrollo de la vocacion de sus alumnos, orientandolos hacia las especialidades que correspondan.


Documento: 15
Articulo: 455
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

La Universidad instituira becas con objeto de lograr la mayor dedicacion de los Estudiantes.


Documento: 15
Articulo: 456
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION C: De los Estudiantes

Toda persona que lo solicite sera inscripta como alumno vocacional en cualquier catedra de una Facultad; podra presentarse a examen y solicitar certificado de curso aprobado. Estos examenes rendidos por alumnos vocacionales no daran opcion a titulo universitario alguno. Cada Facultad reglamentara esta disposicion.


Documento: 15
Articulo: 457
Capitulo: TITULO IV: DE LOS CUERPOS UNIVERSITARIOS. SECCION D: De los Administrativos

El Cuerpo de Administrativos se integra con la totalidad de los agentes Administrativos, Tecnicos, de servicios y mantenimiento que figuren en la planta permanente de la Universidad. Para ser Consejero Administrativo se requiere contar con cinco anos de antiguedad en la Universidad.


Documento: 15
Articulo: 458
Capitulo: TITULO IV: MEDIOS DE REALIZACION

Para cumplir sus objetivos en la docencia y en la investigacion la Universidad propendera a la plena dedicacion de sus Docentes, Investigadores y Alumnos.


Documento: 15
Articulo: 459
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

Los ambitos universitarios deben ofrecer libre acceso a los Estudiantes, Egresados y otras personas que deseen completar conocimientos, conforme a las reglamentaciones que se dicten para su admisibilidad.


Documento: 15
Articulo: 460
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

El ingreso y el desarrollo de la ensenanza de grado, son gratuitos en cualquiera de los establecimientos que integran la Universidad.


Documento: 15
Articulo: 461
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

La Universidad debe impartir los conocimientos, en condiciones que estimulen en los Estudiantes el proceso elaborativo del saber, desarrollando su capacidad de observacion, el espiritu critico, la vocacion cientifica y la responsabilidad moral y social.


Documento: 15
Articulo: 462
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

La ensenanza debe orientarse hacia la formacion integral del hombre, de manera tal, que las actividades que realicen los Graduados, a traves de su trabajo profesional, influya positivamente en el desarrollo cultural de la sociedad.


Documento: 15
Articulo: 463
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

La Universidad reconoce dos formas de realizar la docencia: a) Regular. b) Libre.


Documento: 15
Articulo: 464
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

Docencia regular es la que se realiza en cumplimiento de planes de estudio estructurados por cada Facultad, de acuerdo a los objetivos y normas de la Universidad.


Documento: 15
Articulo: 465
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

La docencia libre consistira: a) En la creacion de cursos libres completos con programas aprobados por el Consejo Directivo. b) En completar o ampliar los cursos oficiales. c) En el desarrollo de puntos o materias que aunque no figuren en los programas de las Facultades, se relacionen con la ensenanza que en ellas se imparte.


Documento: 15
Articulo: 466
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 1: De la Ensenanza

Podran ejercer la docencia libre los Docentes Universitarios y los Diplomados Universitarios Nacionales y Extranjeros o personas de reconocida competencia, previa autorizacion de la Facultad respectiva. Los Consejos Directivos de cada Facultad reglamentaran la forma de autorizar y desarrollar los cursos libres y el contralor de los que fueran paralelos a los oficiales. Las personas autorizadas que hayan dictado cursos libres completos, formaran parte de las respectivas comisiones examinadoras.


Documento: 15
Articulo: 467
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 2: De la Investigacion Cientifica

La Universidad como centro de creacion de conocimientos, fomentara el desarrollo de la investigacion por los siguientes medios: a) Creacion de Institutos de Investigacion. b) Estimulo de la investigacion en las catedras. c) Intercambio de investigadores y creacion de becas de perfeccionamiento. d) Dedicacion exclusiva de sus Docentes a la catedra y la investigacion. e) Intervencion de los alumnos y graduados en las tareas vinculadas a la investigacion, a efectos de desarrollar su capacidad creadora.


Documento: 15
Articulo: 468
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 2: De la Investigacion Cientifica

Para la coordinacion y promocion de la investigacion cientifica funcionara un Consejo de Investigaciones, como asesor del Rector y del Consejo Superior.


Documento: 15
Articulo: 469
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 2: De la Investigacion Cientifica

El Consejo de investigaciones estara integrado por dos delegados por cada Facultad y/o Institutos de Investigacion, avalados por los Consejos Directivos de las mismas, y nombrara un presidente de entre sus miembros. Los miembros seran Profesores y/o Investigadores de la Facultad o Institutos que lo designe. Duraran cuatro anos en sus funciones y podran ser reelectos sin limitacion. El cargo de miembro del Consejo de Investigaciones es honorario.


Documento: 15
Articulo: 470
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 2: De la Investigacion Cientifica

Son funciones del Consejo de Investigaciones: a) Delinear politicas y planes de investigacion y desarrollo en el ambito de la Universidad Autonoma de Entre Rios. b) Disenar los instrumentos y normativas para la evaluacion y seguimiento de las actividades de investigacion. c) Estimular la investigacion por todos los medios que la Universidad ponga a su alcance. d) Presentar anualmente al Rector, al Consejo Superior y a los respectivos Consejos Directivos un informe y el plan de trabajo para el siguiente ano academico. e) Aconsejar la distribucion del fondo de investigacion para cada Facultad, Instituto o Escuela.


Documento: 15
Articulo: 471
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 2: De la Investigacion Cientifica

El Consejo Superior reglamentara el funcionamiento del Consejo de Investigaciones.


Documento: 15
Articulo: 472
Capitulo: TITULO IV: MEDIOS DE REALIZACION. CAPITULO 3: De la Extension Universitaria y Funcion Social

Esta universidad fomenta el desarrollo de la extension universitaria por los siguientes medios: a) Impulsando la interaccion con los otros sectores de la sociedad a partir de su desarrollo academico, cientifico y tecnologico. b) Proponiendo el desarrollo de proyectos con la participacion de los diferentes estamentos de la comunidad universitaria. c) Tendiendo a generar las condiciones e instrumentos que permitan la difusion del conocimiento cientifico-tecnologico y su correspondiente transferencia a los diferentes sectores de la region, desde la logica academica y el propio desarrollo de la institucion. d) Promoviendo la generacion de iniciativas tendientes al estudio y propuestas a los diversos problemas, tanto para el ambito local, nacional o regional. e) Fomentando la participacion en espacios de expresiones artisticas que preserven y promuevan la diversidad cultural de la sociedad. f) Son fines adicionales de la extension universitaria los especificados en las partes pertinentes del Articulo 2 de este Estatuto.


Documento: 15
Articulo: 473
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Bienes de la Universidad

Son bienes de la Universidad: a) Los que constituyen su actual patrimonio. b) Los demas muebles, inmuebles y derechos que ingresen al mismo, a titulo gratuito u oneroso. c) Los recursos que provengan: 1) Del Presupuesto General de la Provincia. 2) De los Presupuestos Generales de la Nacion. 3) De los Presupuestos Generales de las Municipalidades. 4) De las leyes o acuerdos especiales. 5) De los impuestos nacionales, provinciales o tasas municipales. 6) De las contribuciones y subsidios de la Nacion, Provincias y Municipalidades, o que los particulares le destinen. 7) De los legados o donaciones que se reciban de personas o instituciones privadas. 8) De las rentas, frutos o productos e intereses de su patrimonio y el producido por las concesiones y/o recursos derivados de la negociacion de sus bienes por si o por intermedio de terceros. En este ultimo caso se requerira la aprobacion de dos tercios de los miembros presentes del Consejo Superior. 9) De los derechos, aranceles u honorarios que perciba como retribucion de los servicios no Docentes que preste directamente o por intermedio de sus Facultades, Escuelas, Institutos o personas de su dependencia. 10) De los derechos de explotacion de patentes de invencion que se le transfieran y/o derechos intelectuales que pudieran corresponderle por trabajos realizados en su seno. 11) De las contribuciones de los Egresados. 12) De cualesquiera otros fondos que, en forma periodica o no, ingresen a la Universidad.


Documento: 15
Articulo: 474
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Fondo Universitario

Constituyen el fondo universitario: a) Sus bienes actuales. b) El importe de las economias que anualmente se obtengan del presupuesto de la Universidad. c) De los demas valores que la Universidad decida destinarle. d) El producto del o de los impuestos nacionales, provinciales y municipales u otros recursos que se afecten especialmente al mismo. e) Cualesquiera otros fondos que, en forma periodica o no, ingresen al mismo.


Documento: 15
Articulo: 475
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Fondo Universitario

El fondo Universitario sera utilizado exclusivamente para atender las necesidades de la Universidad suscitadas en el cumplimiento de sus objetivos fundamentales: cultura, ensenanza e investigacion que no puedan ser atendidos con los recursos normales del presupuesto.


Documento: 15
Articulo: 476
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Fondo Universitario

El fondo universitario no sera utilizado para rentar funciones permanentes, salvo contratacion de personal Docente o de investigacion, ni tampoco para la atencion de gastos de funcionamientos comunes o normales de la administracion.


Documento: 15
Articulo: 477
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Fondo para Investigacion

A los fines del adecuado cumplimiento de la funcion de investigacion cientifica que compete a las Universidades, crease el fondo de investigacion en cada Facultad e Instituto, el que se formara con los siguientes recursos: a) Con las partidas que anualmente se fijan en el presupuesto de la Universidad. b) Con las partidas especiales que se acuerden a ese fin. c) Con la participacion que se establezca en el Fondo Universitario. d) Con todo otro recurso que ingrese con cargo, cualquiera sea su origen (nacional, provincial, municipal y/o de particulares). En este ultimo caso, se requerira la aprobacion de dos tercios de los miembros presentes del Consejo Superior. e) Con las edonomias de inversion que se obtengan en la asignacion anual de este fondo, que se incorporaran al Fondo Universitario, al solo efecto de ser destinadas anualmente para reforzar presupuestariamente al Fondo de Investigacion.


Documento: 15
Articulo: 478
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Fondo de Propio Producido

Las Facultades, Escuelas o Institutos de la Universidad que puedan obtener recursos de Propio Producido, podran utilizar los mismos dentro de su ambito movilizandolo por via del presupuesto.


Documento: 15
Articulo: 479
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 1: Del Patrimonio y Administracion - Fondo de Propio Producido

Las economias de inversion que se originen en el rubro Fondo de Propio Producido ingresaran al Fondo Universitario con identico criterio al sustentado para el Fondo de Investigacion para ser destinadas a reforzar anualmente la dotacion presupuesta de la Facultad o Instituto que lo produjo.


Documento: 15
Articulo: 480
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 2: De los Cargos Administrativos

Corresponde al Rector nombrar y remover, por si mismo a los empleados dependientes del Consejo Superior y Rectorado, de acuerdo a las reglamentaciones vigentes.


Documento: 15
Articulo: 481
Capitulo: TITULO VI: REGIMEN FINANCIERO Y ADMINISTRATIVO. CAPITULO 2: De los Cargos Administrativos

Corresponde al Decano el nombramiento y remocion del personal de la Facultad, de acuerdo a las reglamentaciones vigentes.


Documento: 15
Articulo: 482
Capitulo: TITULO VII: INCOMPATIBILIDADES

Es incompatible el cargo de Rector con el de Decano y con el de Consejero del Consejo Directivo. Es incompatible el cargo de Consejero del Consejo Superior con el de Consejero del Consejo Directivo.


Documento: 15
Articulo: 483
Capitulo: TITULO VII: INCOMPATIBILIDADES

Los Graduados no podran estar inscriptos en padrones de distintos Cuerpos.


Documento: 15
Articulo: 484
Capitulo: TITULO VII: INCOMPATIBILIDADES

Los miembros Titulares del Consejo Superior y de los Consejos Directivos no podran desempenar empleos Administrativos rentados dependientes de la Universidad. Los miembros Titulares de los Consejos Directivos y del Consejo Superior tampoco podran ser nombrados para catedras, empleos o comisiones rentadas creados durante sus mandatos, antes de transcurrir dos anos de terminado este, excepto en los casos previstos por el Articulo 9, inciso h) de este Estatuto, en lo que hace al personal Docente. Los Consejeros que aspiren a catedras o cargos ya existentes, solo podran presentarse a concurso previa renuncia del cargo de miembro Titular del Consejo. Se exceptuan aquellos cargos obtenidos por Estudiantes, exclusivamente por promedio de calificacion.


Documento: 15
Articulo: 485
Capitulo: TITULO VII: INCOMPATIBILIDADES

Queda suspendida la ciudadania universitaria de Docente universitario contratado, en la Facultad respectiva, durante la vigencia del contrato.


Documento: 15
Articulo: 486
Capitulo: TITULO VII: INCOMPATIBILIDADES

Los cargos de Director y Vicedirector de instituciones anexas de distintos Niveles Educativos son incompatibles con los cargos electivos.


Documento: 15
Articulo: 487
Capitulo: TITULO VII: INCOMPATIBILIDADES

Por ordenanza especial el Consejo Superior reglamentara las incompatibilidades para el ejercicio de los cargos Directivos, Docentes, Tecnicos y Administrativos dentro de la Universidad. El desempeno de la docencia en la Universidad, Facultades, Escuelas, Niveles Educativos, Institutos que dependen de las Facultades de la Universidad, no sera obice a la retribucion que por el ejercicio de actividades profesionales corresponda a los Docentes, aunque la misma estuviera a cargo de la Provincia con motivo de nombramiento de oficio o de condenaciones judiciales. Los Consejeros no podran recibir remuneracion por prestacion de servicios profesionales a la Universidad mientras dure su mandato.


Documento: 15
Articulo: 488
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

El Rector, los Decanos y Directores tendran a su cargo el mantenimiento del orden y la disciplina en sus correspondientes jurisdicciones. Igual atribucion compete a los Profesores en el aula. Las resoluciones podran ser apeladas jerarquicamente ante el Consejo Directivo y el Consejo Superior respectivamente.


Documento: 15
Articulo: 489
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

Se refiere a las facultades del Consejo Superior para suspender al Rector o a cualquiera de sus miembros por causa justificada, siendo causal de suspension el tramite del juicio respectivo, con el voto de sus integrantes. Los Decanos, Vicedecanos y Consejeros, podran ser suspendidos o separados de sus cargos por el Consejo Directivo. La suspension del Rector o Vicerrector se efectuara ad referendum de la Asamblea Universitaria, conforme al Articulo 9o inciso e). El Consejero que dejare de asistir a 3 sesiones consecutivas o a 5 alternadas de las celebradas durante el ano sin permiso del Consejo, dejara de serlo sin necesidad de declaracion alguna.


Documento: 15
Articulo: 490
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

Para la sustanciacion del juicio academico y entender en toda otra cuestion etico-disciplinaria de la totalidad de los Docentes de la universidad, funcionara un Tribunal Universitario y el Consejo Superior reglamentara su composicion y funcionamiento.


Documento: 15
Articulo: 491
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

Los Consejos Directivos podran suspender a los Docentes y solicitar su separacion al Consejo Superior con la intervencion del Tribunal Universitario, por las siguientes causas: a) Condenacion penal. b) Negligencia, inconducta o inasistencia reiterada a clase o examenes. c) Incompetencia. d) Aceptacion de empleo o comisiones incompatibles con el cargo. Esta medida debera ser tomada en sesion especial convocada al efecto con ocho dias de anticipacion con vista previa al Docente, requiriendose para su aprobacion las dos terceras parte de los miembros integrantes del Consejo Directivo y/o Consejo Superior.


Documento: 15
Articulo: 492
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

Todo Docente que faltare a la cuarta parte de sus clases fijada por el horario oficial sin causa justificada sufrira el descuento de tres meses de sueldo, si las faltas llegaren a la tercera parte se le descontara un mes mas. Si sobrepasare la mitad del numero de clases anuales, sin causas justificadas, se considerara que ha cesado automaticamente en su desempeno, debiendo la Facultad comunicarlo al Consejo Superior a los efectos correspondientes. Por cada inasistencia no justificada a las mesas examinadoras el Docente sufrira un descuento del diez por ciento de su sueldo. La inasistencia reiterada a las mismas sera considerada falta grave y los descuentos que se refiere este Articulo ingresaran al fondo universitario. En caso de incumplimiento no justificado de lo dispuesto por el Articulo 58, inciso b) y c), quedaran cesantes sin necesidad de declaracion alguna, debiendo el Decano dar cuenta de la vacante en la primera sesion siguiente del Consejo Directivo. Los Docentes Interinos a que se refiere el Articulo 66 podran ser suspendidos o separados por los Consejos Directivos en la forma prescripta por el Articulo 115.


Documento: 15
Articulo: 493
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

El Consejo Directivo podra apercibir, suspender o separar al Director y Vicedirector de la Escuela anexa por las causas establecidas en el Articulo 115. El Decano solo podra apercibirlo, con cargo de dar cuenta al Consejo Directivo. Por iguales motivos los Profesores de esas Escuelas podran ser apercibidos por el Director y separados o suspendidos por el Consejo Directivo.


Documento: 15
Articulo: 494
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

Por causas de inconducta, previo sumario los Estudiantes de la Universidad, podra sufrir las siguientes sanciones: a) Apercibimiento. b) Suspension. c) Separacion de una Facultad. d) Separacion de la Universidad. En estos dos ultimos casos las mismas seran aplicadas por el Consejo Directivo y por los dos tercios de los votos de sus integrantes, y podra apelarse ante el Consejo Superior. La separacion de la Universidad solo podra ser decretada por el Consejo Superior, previo sumario, y por dos tercios de los votos de sus integrantes. Toda separacion de una Facultad se hara conocer al Consejo Superior, para que este la extienda a la universidad si la considera conveniente.


Documento: 15
Articulo: 495
Capitulo: TITULO VIII: REGIMEN DISCIPLINARIO

El sufragio es obligatorio en todos los casos establecidos en este Estatuto. Los Docentes, Graduados, Estudiantes y Administrativos que no votaran, sin causa justificada, a juicio del Consejo Directivo, incurriran en las sanciones que oportunamente reglamente el Consejo Superior. Iguales sanciones se aplicaran en caso de inasistencia injustificada a la Asamblea Universitaria.


Documento: 15
Articulo: 496
Capitulo: TITULO IX: DISPOSICIONES GENERALES

El quorum de los organos de gobierno de forma colectiva se formara con la mitad mas uno de sus miembros. Las decisiones se adoptaran por simple mayoria, salvo reconsideraciones que requieran dos tercios de votos, o disposicion expresa en contrario. La ausencia voluntaria o el retiro de igual origen, de uno o mas miembros de los Cuerpos Universitarios que integran los organos de gobierno, en ningun caso podra afectar la constitucion o funcionamiento de dichos organos, en tanto mantengan las proporciones que este Articulo requiere precedentemente.


Documento: 15
Articulo: 497
Capitulo: TITULO IX: DISPOSICIONES GENERALES

Estan comprendidas bajo la designacion de Profesores Titulares con iguales derechos y obligaciones las siguientes categorias: a) Titulares. b) Asociados.


Documento: 15
Articulo: 498
Capitulo: TITULO IX: DISPOSICIONES GENERALES

Cada Facultad establecera su regimen de promociones en la ensenanza, de acuerdo a sus planes de estudio y a sus propias exigencias. Los turnos de examenes no deberan obstaculizar el regimen normal de los estudios, debiendo las Facultades dictar normas reglamentarias pertinentes.


Documento: 15
Articulo: 499
Capitulo: TITULO IX: DISPOSICIONES GENERALES

Los Consejos Directivos decidiran sobre las condiciones de elegibilidad de los Estudiantes que cursen carreras no completas al momento de la convocatoria.


Documento: 15
Articulo: 500
Capitulo: TITULO IX: DISPOSICIONES GENERALES

Ningun funcionario o empleado de la Universidad cualquiera fuese su categoria, podra ser separado de sus funciones o puesto sin causa justificada, debidamente comprobada mediante sumario previo.


Documento: 15
Articulo: 501
Capitulo: TITULO IX: DISPOSICIONES GENERALES

Para todos los terminos a que se refiere este Estatuto se contaran unicamente los dias habiles.


Documento: 15
Articulo: 502
Capitulo: TITULO IX: DISPOSICIONES GENERALES

El Rector, los Decanos y los Directores de Escuelas dispondran todas aquellas medidas que permitan en consonancia con lo dispuesto en la Ley 24.521, el libre funcionamiento de los Centros de Estudiantes y Federacion Regional en el ambito de sus respectivas competencias, garantizandose la ubicacion de los locales respectivos en dependencias de las unidades academicas.


Documento: 15
Articulo: 503
Capitulo: TITULO IX: DISPOSICIONES GENERALES

Para los Docentes que al producirse el vencimiento de su periodicidad, estuvieren desempenandose como Consejeros Titulares de los Consejos Directivos y del Consejo Superior, el termino de su periodicidad se cumplira seis meses despues de la terminacion de sus mandatos.


Documento: 15
Articulo: 504
Capitulo: TITULO X: DISPOSICIONES TRANSITORIAS

Mientras no se integren de acuerdo a este Estatuto la totalidad de los estamentos universitarios, el Rector Organizador designara los Decanos Organizadores de las Facultades que integren la Universidad Autonoma de Entre Rios. Los Decanos mientras no se integren los distintos estamentos universitarios de cada Facultad designaran los Directores de las Escuelas Universitarias dependiente de las mismas.


Documento: 15
Articulo: 505
Capitulo: TITULO X: DISPOSICIONES TRANSITORIAS

La Universidad Autonoma de Entre Rios reconoce la antiguedad, estabilidad y haberes del personal Administrativo que se incorpore a la misma provenientes de la Administracion Publica.


Documento: 15
Articulo: 506
Capitulo: TITULO X: DISPOSICIONES TRANSITORIAS

La Universidad Autonoma de Entre Rios reconoce la antiguedad, estabilidad y haberes a los Docentes Titulares que ingresen a la misma provenientes de los establecimientos educacionales publicos transferidos, en todos sus Niveles Educativos dependientes del Consejo General de Educacion de la Provincia de Entre Rios.


Documento: 15
Articulo: 507
Capitulo: TITULO X: DISPOSICIONES TRANSITORIAS

Estos reconocimientos que se mencionan en los Articulos 129 y 130, son tambien a los fines de la integracion de los Cuerpos Organicos de la Universidad y Facultades dependientes de la misma.


Documento: 10002
Articulo: 10001
Capitulo: 

Establecer a partir de la fecha de la presente el Sistema de Adscripciones a Catedras, Proyectos de Extension y de Investigacion para alumnos, egresados y docentes de la Facultad de Ciencia y Tecnologia, que forma parte de la presente Resolucion como ANEXO UNICO.


Documento: 10002
Articulo: 10002
Capitulo: 

Derogar la Resolucion 049/03 F.C. y T. y cualquiera otra norma que se oponga a la presente.


Documento: 10002
Articulo: 10003
Capitulo: 

Registrar, comunicar a quienes corresponda, notificar a las partes interesadas y oportunamente archivar.


Documento: 10002
Articulo: 10005
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. I: DE LA FUNDAMENTACION DEL SISTEMA DE ADSCRIPCIONES

La condicion de adscripto en Docencia, Extension e Investigacion- constituye una de las figuras clasicas de la historia y tradicion universitarias de Occidente en general y del Sistema Universitario de nuestro pais en particular. La creacion de un Sistema general de adscripciones tiene como finalidad fundamental fortalecer la formacion academica y profesional de alumnos, egresados y docentes a traves del desempeno en catedras, proyectos de extension y de investigacion; en el primer caso, de esta Facultad, y, en el segundo, de la propia Universidad y de otras Casas de Altos Estudios. De este modo, la figura del adscripto permite contribuir manifiestamente a la ampliacion, consolidacion y optimizacion estructural del claustro docente y, consecuentemente, a un mejor y superior desarrollo de las funciones de Docencia, Investigacion y Extension de la Facultad de Ciencia y Tecnologia. Asimismo, contribuye significativamente a la formacion de recursos humanos por parte de la propia Facultad en dos sentidos: la actividad del adscripto supone un doble proceso de ensenanza y aprendizaje simultaneos y complementarios entre si: por una parte, el adscripto tiene la posibilidad de brindar una serie de conocimientos especificos propios de su formacion cientifica, y, en su caso, profesionales, y por otro, contribuye mediante un nuevo tipo de aprendizaje- al perfeccionamiento de su propia formacion cientifica, academica y aun profesional; a la vez que le permite adquirir o sumar experiencia en actividades docentes, de extension o de investigacion en una determinada area. Ello asi, los objetivos establecidos para los adscriptos son parcialmente comunes a los fijados para los docentes y para los alumnos de las diversas carreras que se desarrollan en el ambito de la Facultad de Ciencia y Tecnologia.


Documento: 10002
Articulo: 10006
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. II: DEL CARACTER DE LAS ADSCRIPCIONES

La adscripcion a la que se refiere el presente marco regulatorio tendra, a todos los efectos, el caracter de "ad-honorem", no reconociendose derecho alguno a percibir o reclamar ningun tipo de retribucion o remuneracion por el desempeno de la misma. La condicion de adscripto no podra interpretarse en el sentido de producir por si misma derecho alguno a designacion efectiva, rentada o no, de ninguna indole.


Documento: 10002
Articulo: 10007
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. III: DE LAS CATEGORIAS

Se establecen las siguientes categorias de adscriptos para catedras, proyectos de extension y proyectos de investigacion: 1- Egresados con titulacion universitaria de grado o post-grado, ya sea de universidades nacionales o extranjeras, tanto de gestion publica como privada. 2- Egresados de institutos superiores no universitarios, en carreras de no menos de (4) cuatro anos de duracion. 3- Estudiantes universitarios: a los efectos del presente Sistema de Adscripciones, se consideraran en esta categoria a aquellos alumnos regulares que: a) revistan en dicha condicion en alguna de las carreras que se dictan en la Facultad de Ciencia y Tecnologia; b) hayan aprobado la asignatura objeto de la adscripcion con calificacion no inferior a (9) nueve; c) acrediten haber aprobado por lo menos un tercio de las materias que conforman el plan de estudios de la carrera que cursan, con un promedio general igual o superior a (8) ocho.


Documento: 10002
Articulo: 10008
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. IV: DE LAS CONVOCATORIAS

La Facultad de Ciencia y Tecnologia, en el marco de la modalidad de concursos abiertos, llamara inscripcion para adscripciones ya sea para alumnos o graduados; tanto a Catedras como a Proyectos de Extension y de Investigacion- en los meses de marzo y de agosto de cada Ano Academico. Por unica vez y exclusivamente para el presente Ano Academico, el llamado previsto para el mes de agosto se verificara en el mes de septiembre de 2005.


Documento: 10002
Articulo: 10009
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. V: DE LAS CONVOCATORIAS EXTRAORDINARIAS PARA ADSCRIPCIONES A PROYECTOS DE I

Sin perjuicio de lo establecido en el punto precedente, la Facultad podra llamar a inscripcion para adscripciones a Proyectos de Extension o Investigacion fuera de los meses establecidos en el punto anterior, toda vez que las fechas de presentacion, evaluacion, aprobacion y ejecucion de los mismos lo hagan aconsejable.


Documento: 10002
Articulo: 10010
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. VI:DE LAS SOLICITUDES

El postulante a revistar en la condicion de adscripto debera formalizar una solicitud al efecto, por ante la Secretaria Academica de la Facultad de Ciencia y Tecnologia. En la misma indicara la Catedra o Proyecto en que desea realizar la adscripcion y el nombre del titular del mismo. Ademas, adjuntara su curriculum vitae con mas las respectivas constancias. En sobre separado, cerrado y rubricado, remitira su propuesta de Plan de Trabajo, el que debera contener los objetivos y la explicitacion exhautiva del mismo, de modo tal que permita al Comite de Admision colegir su admisibilidad. Eventualmente, podra incluir en la documental presentada un aval del titular de la catedra o proyecto. No procedera la inscripcion en mas de una adscripcion por vez.


Documento: 10002
Articulo: 10011
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. VII: DE LAS ADMISIONES

La incorporacion de adscriptos a una catedra o proyecto sera resuelta por el Comite de Admision de Adscripciones a Catedras, Proyectos de Investigacion y de Extension de la Facultad de Ciencia y Tecnologia. El Comite de Admision estara integrado: a) Si se trata de una Catedra: por el Secretario Academico, quien ejercera la presidencia del mismo; el Titular de la catedra involucrada; el Responsable de Carrera a la que pertenece la asignatura y tres docentes designados al efecto. b) Si se trata de de un proyecto de Investigacion: por el Secretario Academico, quien ejercera la presidencia del mismo; el Secretario de Investigacion; el Responsable del proyecto y tres docentes designados al efecto. c) Si se trata de de un proyecto de Extension: por el Secretario Academico, quien ejercera la presidencia del mismo; el Secretario de Extension; el Responsable del proyecto y tres docentes designados al efecto. Para la aceptacion de las solicitudes, el Comite de Admision tendra en cuenta las siguientes pautas y criterios: Las cualidades intrinsecas del Plan de Trabajo propuesto. Los antecedentes cientificos, academicos, profesionales y culturales del postulante. La viabilidad material y la factibilidad de su realizacion. La relevancia en orden al desenvolvimiento academico y cientifico de la Facultad. La contribucion a la interaccion de la Universidad con la sociedad a traves de la transferencia de conocimientos. La generacion de conocimientos en el marco del plan de investigacion cientifica y desarrollo tecnologico de la Facultad de Ciencia y Tecnologia. En caso de considerarlo necesario, el Comite podra entrevistar al postulante. El Comite de Admision debera pronunciarse, mediante dictamen fundado, en un plazo que no podra exceder los diez (10) dias habiles a partir de la fecha de cierre de la inscripcion. En caso de disconformidad con el decisorio del Comite -que debera ser publicado durante tres dias habiles- el aspirante podra interponer, dentro de los (5) cinco dias habiles posteriores a la publicacion de los resultados, un recurso unico de reconsideracion por ante el Decano Organizador, quien constituyendose en instancia unica de apelacion y sobre la base de las actuaciones producidas, de las constancias obrantes y de los elementos que eventualmente aporte el recurrente, ratificara o rectificara, dando razon, el dictamen del Comite de Admision.


Documento: 10002
Articulo: 10012
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. VIII: DE LAS DESIGNACIONES

Las designaciones se efectuaran mediante resolucion del Sr. Decano Organizador de acuerdo al dictamen del Comite de Admision.


Documento: 10002
Articulo: 10013
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. IX: DE LA DURACION

En el caso de de que la adscripcion se verifique a una catedra, la misma tendra una duracion de dos (2) anos. Para el caso de adscripcion a un proyecto, la duracion de la misma coincidira con la del proyecto.


Documento: 10002
Articulo: 10014
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. X: DEL DIRECTOR DE LA ADSCRIPCION

El docente titular de la Catedra o el Director del Proyecto de Extension o de Investigacion, segun corresponda, sera el Director de la Adscripcion. Conjuntamente con el aspirante a adscripto elaboraran un Plan de Trabajo definitivo que debera ser elevado al Responsable de Carrera y a la Secretaria Academica de la Facultad.


Documento: 10002
Articulo: 10015
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. XI: DE LOS DERECHOS Y OBLIGACIONES

XI.I DE LOS ADSCRIPTOS 1- Cumplir en tiempo y forma con las actividades previstas en el plan de trabajo. 2- Dedicar a la adscripcion un tiempo en la institucion no inferior a la carga horaria de la asignatura o del proyecto. 3- Actuar como docente auxiliar honorario bajo la supervision del titular- en el dictado de la catedra. 4- Asistir a los alumnos en la realizacion de los trabajos practicos, en la elaboracion de guias de estudio teorico-practicas y en otras actividades que determine el titular de la catedra. 5- Presenciar examenes. 6- Disponer de la infraestructura y de los medios instrumentales necesarios para el desarrollo de sus actividades. 7- En los casos que la adscripcion se verifique en proyectos de Extension o de Investigacion, el adscripto debera participar sistematicamente de las acciones inherentes a los mismos, de acuerdo a las determinaciones previamente establecidas en el Plan de Trabajo definitivo. 8- Concurrir como minimo al ochenta por ciento de las instancias presenciales previstas en el plan de trabajo. 9- Registrar la asistencia en las planillas destinadas a tal fin. 10- Elaborar y elevar semestralmente al Director de la adscripcion un informe de avance, detallando el estado de desarrollo de las actividades realizadas, fundamentando en cada caso su contenido y alcances. En el caso de proyectos de investigacion o de extension, este plazo sera acordado entre el adscripto y el titular del proyecto. 11- Elaborar y elevar anualmente al Director de la adscripcion un informe de avance sobre el Trabajo Final. En el caso de proyectos de investigacion o de extension, este plazo sera acordado entre el adscripto y el titular del proyecto. 12- En los casos de adscripciones a catedras, finalizado el segundo ano, el titular de la misma debera presentar al Director de la adscripcion el Trabajo Final, que podra ser un Trabajo de Investigacion. Debera cumplimentar los requisitos inherentes a la naturaleza del mismo, juntamente con un informe anexo que versara sobre la problematica de la catedra o del proyecto y que abarcara los aspectos cientificos y pedagogicos de la misma y formulara propuestas especificas; ademas de sugerencias y alternativas de mejoramiento de los aspectos cientificos, metodologicos y pedagogico- didacticos, segun corresponda. 13- Cuando las adscripciones se verifiquen en Proyectos de Investigacion o de Extension, los plazos para los informes de avance y para el Trabajo Final y las condiciones de los mismos se estableceran en funcion de las caracteristicas del proyecto y de la extension prevista para el mismo. XI.II DE LOS TIULARES DE CATEDRAS, PROYECTOS DE EXTENSION O DE INVESTIGACION: 1- Dirigir y supervisar el proceso de la adscripcion durante todo su desarrollo. 2- Orientar y prestar al adscripto la colaboracion necesaria para la realizacion del plan de adscripcion. 3- Elevar semestralmente al Responsable de Carrera y a la Secretaria Academica un informe sobre el desarrollo de la adscripcion. En los casos de adscripciones a proyectos de investigacion o extension, este plazo se establecera en funcion de la duracion del proyecto. 4- Elevar al Responsable de Carrera o, en su caso, al Secretario de Extension o al Secretario de Investigacion- y a la Secretaria Academica al termino de la adsripcion un informe final en el que debera adjuntar el Trabajo Final del adscrito, la aprobacion de este ultimo junto al concepto merecido. 5- Avalar, si correspondiese, los informes presentados por el adscripto. 6- Solicitar al Responsable de Carrera y a la Secretaria Academica la caducidad de la adscripcion en caso de incumplimiento de cualesquiera de las obligaciones previstas en el apartado Derechos y obligaciones del Adscripto. Para el caso de adscripciones a proyectos de investigacion o de extension, dicha solicitud debera ser elevada al Secretario de Investigacion o al Secretario de Extension, segun corresponda.


Documento: 10002
Articulo: 10016
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. XII: DE LAS CAUSALES DE CADUCIDAD DE LAS ADCRIPCIONES

Seran causales de caducidad de la adscripcion y de eviccion de la condicion de adscrito la falta de cumplimiento, total o parcial, de cualesquiera de los topicos previstos en el presente instrumento legal. Si eventualmente el incumplimiento se debiera a causas extraordinarias o excepcionales, manifiestamente ajenas a la responsabilidad del adscripto y fueran debidamente justificadasy acreditadas a juicio del Director de la Adscripcion, el Sr. Decano Organizador, mediante resolucion expresa, podra autorizar por unica vez, el reinicio o continuidad de la misma. En el caso de los alumnos adscriptos, la perdida de la condicion de regular o el egreso de la carrera sera causal de caducidad automatica. Los casos o situaciones no contemplados en la presente reglamentacion seran resueltos subsidiariamente por el Sr. Decano, sobre la base del informe que al efecto producira la Secretaria Academica, debiendo la misma dar previamente intervencion a las partes involucradas, conforme a los procedimentales establecidos por la Universidad.


Documento: 10002
Articulo: 10017
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. XIII: DEL PLAZO DE ENTREGA DEL TRABAJO FINAL

El plazo de entrega del Trabajo Final sera acordado por el Director de la adscripcion y el adscripto, no pudiendo tal circunstancia exceder el termino de sesenta dias corridos, computados desde el momento de la finalizacion de la adscripcion.


Documento: 10002
Articulo: 10018
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. XIV: DE LA PUBLICACION DEL TRABAJO FINAL

El trabajo final podra ser publicado por la Universidad Autonoma de Entre Rios, previa cesion de derechos de autor, en relacion a la primera edicion, formalizada ante escribano publico.


Documento: 10002
Articulo: 10019
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. XV: DE LA APROBACION DE LAS ADSCRIPCIONES

El Trabajo Final a que se refiere el punto X sera evaluado en forma oral por un Tribunal constituido al efecto. Estara integrado por: a) Si se trata de una Catedra: el titular de la Catedra; el Coordinador de la Carrera; dos (2) docentes designados por la Secretaria Academica, el Decano de la Facultad de Ciencia y Tecnologia, quien presidira el Tribunal. b) Si se trata de un Proyecto de Investigacion: el titular del proyecto; el Secretario de Investigacion; dos (2) docentes designados por la Secretaria Academica, el Decano de la Facultad de Ciencia y Tecnologia, quien presidira el Tribunal. c) Si se trata de un Proyecto de Extension: el titular del proyecto; el Secretario de Extension; dos (2) docentes designados por la Secretaria Academica; el Decano de la Facultad de Ciencia y Tecnologia, quien presidira el Tribunal.


Documento: 10002
Articulo: 10020
Capitulo: SISTEMA DE ADSCRIPCIONES A CATEDRAS, PROYECTOS DE EXTENSION Y PROYECTOS DE INVESTIGACION PARA ALUMNOS, EGRESADOS Y DOCENTES. XVI: DE LA CERTIFICACION DE LAS ADSCRIPCIONES

Aprobada que fuere la evaluacion de la adscripcion, el Decano, con la intervencion de la Secretaria Academica, extenderan al interesado el certificado correspondiente en el que constara que ha cumplido con las condiciones de la adscripcion, detallandose las actividades desarrolladas, el concepto o calificacion obtenida; todo lo cual se fundamentara en los informes del titular de la catedra o, en su caso, de los titulares de los proyectos de extension o investigacion y demas constancias obrantes en las actas confeccionadas al efecto.


Documento: 10003
Articulo: 10021
Capitulo: 

Apruebese el Instructivo para la Tramitacion de Diplomas para egresados de las distintas carreras de la FCyT, en los terminos que se detallan en su cuerpo principal y en sus Anexos I, II, III, IV, V, VI y VII.


Documento: 10003
Articulo: 10022
Capitulo: 

Registrese, comuniquese a quienes corresponda, notifiquese a la parte interesada y oportunamente archivese.


Documento: 10004
Articulo: 10023
Capitulo: 

Rectifiquese la Resolucion No 377/06, de la Facultad de Ciencia y Tecnologia, de la Universidad Autonoma de Entre Rios, segun se detalla a continuacion: Profesorado de Educacion Tecnologica: Agregar en el cuadro demostrativo. TECNO-CIENTIFICO Proyecto Tecnologico III. Profesorado de Quimica: Rectificar. Profesorado de Quimica Donde dice: Pobabilidad y Debe decir: Probabilidad y Estadistica Donde dice: Metodologia de la Debe decir: Metodologia de la Investigacion Educativa.


Documento: 10004
Articulo: 10024
Capitulo: 

Registrese, comuniquese a quienes corresponda, notifiquese a la parte interesada y oportunamente archivese.


Documento: 10005
Articulo: 10025
Capitulo: 

Incluyase en la Resolucion No 2181/09 de la Facultad de Ciencia y Tecnologia referente al Calendario Academico 2010-2011, las fechas de entrega de Planes de Catedra. Programas de Catedra y Memorias de Catedra, en un todo de acuerdo con el Anexo Unico de la presente.


Documento: 10005
Articulo: 10026
Capitulo: 

Registrese, comuniquese a quienes corresponda, notifiquese a la parte interesada y oportunamente archivese.


Documento: 10006
Articulo: 10027
Capitulo: 

Aprobar el Reglamento de TESIS para las LICENCIATURAS que se dictan en esta Universidad Autonoma, el que como Anexo unico pasa a formar parte de la presente Resolucion.


Documento: 10006
Articulo: 10028
Capitulo: 

Registrese, comuniquese, elevese y notifiquese a quien corresponda, cumplido archivese.


Documento: 10006
Articulo: 10030
Capitulo: Capitulo Unico. Disposiciones Generales.

El presente reglamento regira para toda la Universidad Autonoma de Entre Rios y sus disposiciones son obligatorias, de orden publico e interes academico. Su aplicacion y vigilancia corresponden a los alumnos, profesores, directores de carreras, decanos, secretarios academicos y demas autoridades universitarias.


Documento: 10006
Articulo: 10032
Capitulo: Capitulo Unico. Disposiciones Generales.

Este reglamento tiene por objetivo establecer las normas basicas en materia de elaboracion de tesis y que deberan observarse en: a) todo lo conducente al trabajo en si, a su formato y presentacion, b) la determinacion de tipos de tesis y sus caracteristicas mas generales, c) las formalidades y papeles desempenados por los diferentes participantes en el proceso, o sea alumnos tesistas, directores de tesis, codirectores, asesores, jurados, autoridades academicas y administrativas, d) el manejo institucional de la tesis y sus derechos o aportaciones derivadas asi como sus productos, pecuniarios o no, e) creacion, manejo y aplicacion de la legislacion universitaria relacionada con los procesos y aspectos arriba mencionados.


Documento: 10006
Articulo: 10033
Capitulo: Capitulo Unico. Disposiciones Generales.

Este reglamento fija las normas mas generales, cuya observacion es obligatoria para toda la Universidad Autonoma de Entre Rios. Estas normas son de caracter general y basicas, regulando aspectos globales para el conjunto de la comunidad universitaria.


Documento: 10006
Articulo: 10034
Capitulo: Capitulo Unico. Disposiciones Generales.

Toda norma, disposicion o regla que contravenga al presente reglamento se tendra por no escrita.


Documento: 10006
Articulo: 10035
Capitulo: De la Tesis. Capitulo I. Alcances, Conceptos y Objetivos de la Tesis.

La tesis tiene por finalidad explicar, describir, informar, predecir o proponer un descubrimiento, una innovacion, una idea u obra (incluyendo prototipos), o bien un proceso y/o el resultado de una investigacion realizada.


Documento: 10006
Articulo: 10036
Capitulo: De la Tesis. Capitulo I. Alcances, Conceptos y Objetivos de la Tesis.

Ademas de cubrir los requisitos de forma que mas adelante se senalan, las tesis deben tener ciertas cualidades, entre otras, originalidad y novedad; entendiendo para los efectos del presente reglamento, como originalidad a la caracteristica en virtud de la cual el tema desarrollado es diferente, al menos en algun aspecto, a todo lo ya consignado por escrito. La novedad concierne a la concepcion y enfoque y no al tema mismo que puede haber sido objeto de estudio en multiples ocasiones y sin embargo no haber sido analizado en la forma en que lo hace la nueva tesis sino hasta entonces.


Documento: 10006
Articulo: 10037
Capitulo: De la Tesis. Capitulo I. Alcances, Conceptos y Objetivos de la Tesis.

La Secretaria Academica de las respectivas Facultades y el jurado examinador buscaran que las tesis contengan elementos, o se reconozcan en su texto aspectos como los que se enuncian en las siguientes fracciones: I. Hechos objetivos, suprimiendo en lo posible los juicios de valor personales o las proposiciones no sustentadas ni demostradas. II. El manejo adecuado de la metodologia de cada area del conocimiento, ubicando los hechos y sistematizandolos dentro de su contexto logico. III. Siguiendo una manera precisa para lograrlo preestablecida y de comun aceptacion para cada area del conocimiento. IV. Mediante ciertas tecnicas, que sean las mas aceptadas para el metodo seleccionado. V. Con apoyos instrumentales adecuados. VI. Concretados en una aportacion a un area especifica del conocimiento.


Documento: 10006
Articulo: 10038
Capitulo: De la Tesis. Capitulo I. Alcances, Conceptos y Objetivos de la Tesis.

La Secretaria Academica y el jurado examinador buscaran que el (o los) tesista(s) desarrollen las habilidades y capacidades academicas que se enuncian en las siguientes fracciones: I. Identificar y diagnosticar problemas especificos dentro de su area de competencia. II. Proponer soluciones viables, a traves de la sistematizacion y aplicacion de los conocimientos adquiridos a lo largo de sus estudios. III. Analizar criticamente y ponderar tanto la informacion a su alcance, como los recursos, metodos, tecnicas y/o modelos para llegar creativamente a la mejor solucion de un problema o reto en su area especifica de conocimiento. IV. Ser capaz de consignar su estudio o investigacion por escrito con la claridad y requerimientos formales propios del area investigada.


Documento: 10006
Articulo: 10039
Capitulo: De la Tesis. Capitulo I. Alcances, Conceptos y Objetivos de la Tesis.

Para los efectos del presente reglamento se consideran los siguientes tipos principales de tesis: I. De Aplicacion. Es un documento escrito cuyo proposito es resolver un problema real, proponer acciones alternativas de solucion a un problema o explicar un fenomeno, mediante la aplicacion de tecnicas y/o metodologia especificas. II. Monografica. Es un documento escrito cuyo proposito es analizar y sintetizar un area especifica del conocimiento, aportando, en algunas ocasiones, nuevas lineas de investigacion. III. Teorica. Es un documento escrito cuyo proposito consiste en el desarrollo de una linea de


Documento: 10006
Articulo: 10040
Capitulo: De la Tesis. Capitulo I. Alcances, Conceptos y Objetivos de la Tesis.

La tesis constituye el ultimo trabajo academico del estudiante de licenciatura y el primero a nivel profesional en su area, por lo que debera contemplar lo senalado en las siguientes fracciones: I. Ser integradora de los conocimientos y habilidades adquiridas. II. Requerir procesos de analisis y sintesis y/o evaluacion del tema que se desarrolle. III. Evicenciar la actitud critica del tesista. IV. Contribuir en su area, entre otros aspectos, con el tratamiento original del tema, proporcionar informacion relevante, o bien la solucion teorico-practica a un problema especifico. V. Proporcionar una oportunidad para que el alumno ordene, sistematice y aplique conocimientos adquiridos y para que los transforme en un producto nuevo o para resolver un problema nuevo. VI. Seguir una metodologia propia del area que aborda. VII. Tener un sustento teorico relevante. VIII. Presentarse como un trabajo de investigacion formal con los elementos reconocidos para tal caso dentro del area academica de que se trate.


Documento: 10006
Articulo: 10041
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

La Secretaria Academica de las respectivas Facultades, acorde a los Planes de Estudios, fijara los requisitos que los estudiantes de su(s) carrera(s) deberan cumplir para poder inscribirse en la asignatura de TESIS o equivalente, pudiendo basarse en: I. Numero de unidades aprobadas de la carrera. II. Numero de materias que faltan cursar de la carrera. III. Ademas de los requisitos anteriores, el cursar ciertos materias que sean de importancia especifica para el desarrollo del proyecto en que el estudiante desea involucrarse.


Documento: 10006
Articulo: 10042
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

Toda tesis podra ser realizada individualmente o en equipo. Cada Carrera establecera el numero maximo de integrantes para tesis colectivas.


Documento: 10006
Articulo: 10043
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

Para la adecuada proteccion del tesista, la Secretaria Academica tendra las siguientes responsabilidades: I. Asegurarse que el alumno siempre cuente con el apoyo de los academicos necesarios para el desarrollo de su tesis. II. En caso de que algun academico no pueda seguir con la funcion asignada, la Secretaria Academica vera que a la brevedad posible sea sustituido, tramitando la formalizacion ante el Consejo Directivo. III. En cualquier caso de incumplimiento del Director de tesis, buscara una solucion adecuada para el tesista.


Documento: 10006
Articulo: 10044
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

Si despues de que se ha asignado un director de tesis a un estudiante, este desea que la direccion del desarrollo del proyecto se asigne a otra persona, debera plantear su peticion por escrito a la Secretaria Academica quien analizara la factibilidad de tal peticion, considerando entre otras cosas, el interes de la persona en quien se desea recaiga la responsabilidad y su carga de trabajo.


Documento: 10006
Articulo: 10045
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

Durante el desarrollo del proyecto y hasta antes de la presentacion del reporte escrito al jurado examinador, se podran plantear y hacer correcciones sustanciales al contenido del proyecto, siempre y cuando, el estudiante presente la solicitud en forma escrita a su Director de Tesis, el mismo este de acuerdo y ademas sea avalado por la Secretaria Academica y aprobado por el Consejo Directivo.


Documento: 10006
Articulo: 10046
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

Frente a cualquier solicitud de modificacion del contenido de proyecto, la Secretaria Academica, contestara tambien en forma escrita al estudiante, informandole del resultado de su solicitud.


Documento: 10006
Articulo: 10047
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

Cuando se acepten las modificaciones al contenido de un proyecto, el estudiante debera elaborar y entregar las copias necesarias de este, a fin de que el registro que se tenga del contenido, sea el mismo para el estudiante y la Secretaria Academica.


Documento: 10006
Articulo: 10048
Capitulo: De la Tesis. Capitulo II. Aspirantes a Tesis y Cuestiones Relativas a los Estudiantes.

En aquellos casos en que el alumno decida cambiar de tema, por causas no impotables a la Universidad, todas las consecuencias y trabajo que de este hecho se deriven seran de su total incumbencia. Ante todo debera someter su peticion por escrito para el cambio de tema y esperar el tiempo necesario para que el Consejo Directivo decida al respecto.


Documento: 10006
Articulo: 10049
Capitulo: De la Tesis. Capitulo III. De la Propuesta, su aprobacion y modificaciones; del Proyecto.

La evaluacion de la propuesta de tesis sera competencia de la Secretaria Academica de cada Facultad. La evaluacion de la propuesta se basara en los criterios que cada Carrera fije al respecto.


Documento: 10006
Articulo: 10050
Capitulo: De la Tesis. Capitulo III. De la Propuesta, su aprobacion y modificaciones; del Proyecto. De la propuesta.

Para la aprobacion de la propuesta de tesis se observaran los siguientes procedimientos y formas: I. De la Inscripcion. El estudiante debera someter su propuesta de tesis a la Secretaria Academica de la Facultad respectiva, siguiendo un formato preestablecido, quien con la respectiva evaluacion la elevara al Consejo Directivo para su aprobacion. II. De acuerdo con la fraccion anterior, la propuesta se considerara inscripta por un plazo maximo de dos anos; transcurrido ese plazo el alumno podra solicitar una prorroga adicional de un ano, que el Consejo Directivo concedera unicamente si el tema conserva su relevancia academica y social. III. Del periodo para la presentacion. La Secretaria Academica definira y difundira al comiendo de cada ano academico, el periodo para la presentacion de las propuestas, asi como el formato oficial y los demas requisitos que considere necesarios para someter la propuesta a la aprobacion del Consejo Directivo. IV. De la aprobacion. El Consejo Directivo aprobara las propuestas de tesis cuando cumplan con los requisitos establecidos en la normatividad respectiva. Existira aprobacion condicional cuando solo se requieren correcciones o ajustes que no alteren en lo fundamental a la propuesta. Para su aprobacion definitiva las propuestas condicionadas deberan de haber sido corregidas de acuerdo a las indicaciones de la primera revision correspondiendo al Director de Tesis el verificar que tales correcciones se hagan. Los plazos para este tramite no podran en ningun caso exceder a los quince dias habiles. V. De las propuestas rechazadas. En caso de que la propuesta sea rechazada se exigira el que se elabore una propuesta totalmente nueva. El plazo para someter una nueva propuesta y para que esta sea considerada dentro del mismo ciclo academico no debera exceder a los treinta dias habiles. VI. De la modificacion posterior de Propuestas ya aprobadas. En los casos en que se pretendan modificaciones sustanciales a la tesis, tales como cambios en los objetivos y alcances de la propuesta inicial, metodologia a seguir o cambios en los estudiantes realizadores de la investigacion, se debera lograr la aprobacion escrita del Consejo Directivo. Este contara a lo mas con diez dias habiles para estudiar y contestar a la solicitud de cambios.


Documento: 10006
Articulo: 10051
Capitulo: De la Tesis. Capitulo III. De la Propuesta, su aprobacion y modificaciones; del Proyecto. De la propuesta.

Partes de la Propuesta. La propuesta debera incluir al menos las siguientes partes: Portada: Tema de la propuesta. Director y asesores (en el caso de requerirlo) sugeridos; Cuerpo: Breve descripcion Justificacion. Programa o calendario de Actividades. Bibliografia Inicial. Estos conceptos son detallados en las siguientes fracciones: I. Tema.- El tema debera expresar lo mas claramente posible la finalidad de la propuesta. El tema no es el titulo final de la investigacion sino una aproximacion o ubicacion conceptual acerca de lo que se pretende trabajar. II. Nombre(s) y datos. La propuesta podra presentarse individualmente o en equipo. En cualquier caso se deberan presentar los datos del (los) estudiante(s) tesista(s): Nombre, Matricula de estudiante, direccion y telefono. III. Fecha de presentacion de la propuesta.- Correspondera al dia en que se someta la propuesta a la aprobacion del Consejo Directivo. IV. Director y asesores. El estudiante podra solicitar o proponer a los miembros del departamento academico que considera mas idoneos. La Secretaria Academica tomara en cuenta esta solicitud para determinacion del director y asesores de la tesis en caso en que se requiriesen. V. Breve descripcion. En forma clara y concisa el estudiante explicara el tema objetivo de su propuesta. VI. Justificacion.- En forma clara y concisa el estudiante proporcionara los elementos que hacen que el tema propuesto sea relevante para su area de estudio. VII. Programa o calendario de actividades.- El trabajo a realizar se debera desglosar en actividades particulares, senalando las fechas de inicio y terminacion de las mismas. VII. Bibliografia inicial.- Se indicaran las fuentes bibliograficas o documentales pertinentes al tema propuesto.


Documento: 10006
Articulo: 10052
Capitulo: De la Tesis. Capitulo III. De la Propuesta, su aprobacion y modificaciones; del Proyecto. De la propuesta.

Cada Carrera podra ampliar la lista anterior si lo considera necesario. Algunos puntos adicionales que se pueden considerar son: - Objetivo general. - Objetivos especificos. - Alcances y limitaciones. - Material y equipo. - Plan de Investigacion. - Estructura (Contenido Tentativo). - Autorizacion de Derechos de Autor. - Metodos y tecnicas. - Otros aspectos, de acuerdo al criterio del departamento. I. Objetivo general. Indicacion breve del proposito del tema propuesto. II. Objetivos especificos. Establecer los propositos particulares para alcanzar el objetivo general; son los elementos constitutivos del objetivos general. III. Alcances y limitaciones. En este apartado se explica con exactitud que se planea cubrir con la investigacion propuesta. Especificando las areas del conocimiento cubiertas y las que no se incluiran o tocaran. IV. Material y equipo. Se debera especificar el material, equipo y cualquier otro recurso fisico que se requerira para alcanzar los objetivos propuestos, senalando la fuente o entidad idonea para su obtencion. V. Plan de investigacion. Se debera identificar y definir las fases del proyecto, tales como: diseno de la investigacion, recopilacion de la informacion, procesamiento de datos, experimentacion, entre otros. VI. Estructura. El trabajo se dividira en la misma forma como se presentara el reporte final, es decir por capitulos. VII. Automatizacion de derechos de autor. Este apartado seguira lo establecido en los articulos del capitulo cuarto de ese mismo reglamento. VIII. Metodos y tecnicas. En este apartado se debera identificar y justificar los metodos y/o tecnicas a emplear para la consecucion del objetivo general de la propuesta.


Documento: 10006
Articulo: 10053
Capitulo: De la Tesis. Capitulo IV. De los Derechos de Autor.

El estudiante que elabora una tesis en la Universidad Autonoma de Entre Rios produce un documento publico, que por definicion sirve para consulta y/o divulgacion de conocimientos e ideas; su uso o aprovechamiento academico por terceros solo estara restringido por la observancia de las normas de manejo bibliografico y documental en los terminos eticos de aceptacion internacional.


Documento: 10006
Articulo: 10054
Capitulo: De la Tesis. Capitulo IV. De los Derechos de Autor.

La autorizacion que el estudiante otorgue para el aprovechamiento academico de su tesis debera quedar registrada en la propuesta, acompanada de la(s) firma(s) del (los) autor(es).


Documento: 10006
Articulo: 10055
Capitulo: De la Tesis. Capitulo IV. De los Derechos de Autor.

Cuando el alumno se incorpore a un proyecto de investigacion o proceso ya establecido o determinado por otros, se convertira en un instrumentador, desarrollador o colaborador, sin derechos de autoria, los cuales perteneceran a quien haya concebido el proyecto de investigacion. En tal caso, el alumno no podra demandar mayor beneficio que el de ser citado como colaborador, lo que debera quedar registrado en la propuesta.


Documento: 10006
Articulo: 10056
Capitulo: De la Tesis. Capitulo IV. De los Derechos de Autor.

Cuando el alumno elabore una tesis en la que se lleguen a presentar prototipos, creaciones o tecnologia totalmente nueva, el sera el legitimo propietario de cualquier producto, derivado, beneficio o resultado que se obtenga como consecuencia de su proyecto. Esto ultimo no lo exime de permitir el uso adecuado de su tesis para fines academicos o de divulgacion del conocimiento lo que debera quedar registrado en la propuesta.


Documento: 10006
Articulo: 10057
Capitulo: Del Director de Tesis.

El Director de la tesis sera propuesto por el estudiante y ser profesor en ejercicio de la Universidad Autonoma de Entre Rios, preferentemente de la carrera del postulante y tener, en lo posible, una especialidad afin al tema. Si no hubiese un profesor de la Universidad relacionado con el tema de investigacion o no existieran profesores disponibles, el postulante podra proponer a profesores de otras Universidades Nacionales. Su funcion sera la de conducir el desarrollo general y especifico del proyecto y de la tesis.


Documento: 10006
Articulo: 10058
Capitulo: Del Director de Tesis.

Las condiciones academicas, profesionales y cualquier otra caracteristica del Director de Tesis seran establecidas por la Secretaria Academica. En todos los casos debera poseer un grado academico igual o superior al que postula el estudiante.


Documento: 10006
Articulo: 10059
Capitulo: Del Director de Tesis.

En el caso de que el Director de Tesis por cualquier razon ya no pueda seguir dirigiendo ese proceso academico, la Secretaria Academica se encargara de proponer un nuevo director y elevara su propuesta para la aprobacion del Consejo Directivo.


Documento: 10006
Articulo: 10061
Capitulo: Del Director de Tesis.

El Director de tesis sera el unico canal para el avance y modificaciones al proyecto original de investigacion y tesis. Esto incluye la exigencia para los tesistas de que cualquier contacto con los otros academicos debe ser autorizada y con la participacion del Director.


Documento: 10006
Articulo: 10062
Capitulo: Del Director de Tesis.

Las funciones del Director de Tesis son: I. Orientar al estudiante a fuentes de informacion adecuadas. II. Establecer con el estudiante las fechas y horas de asesoria, entrega de reportes de avance, revision del reporte escrito y otros; ademas controlara el cumplimiento del programa de actividades. III. Supervisar que el proyecto se este desarrollando con la calidad esperada, considerando que es responsabilidad del estudiante la obtencion de resultados satisfactorios. IV. Discutir y en su caso sugerir de comun acuerdo con el(los) tesista(s) las modificaciones a la propuesta, debiendo presentar por escrito la solicitud de modificacion a la Secretaria Academica a la brevedad posible; esto se tendra que hacer antes de la presentacion del reporte final.


Documento: 10006
Articulo: 10063
Capitulo: Del Director de Tesis.

Es responsabilidad del director de tesis decidir si el alcance y los objetivos del Proyecto han quedado satisfechos para dar el curso a la presentacion del reporte final. De no ser asi el director tiene la potestad de negar la presentacion del reporte final.


Documento: 10006
Articulo: 10064
Capitulo: Del Director de Tesis.

Ademas de lo anterior y para efectos academico-administrativos, el Director de Tesis: I. Evaluara los reportes de avance y los reportara al titular de la Catedra TESIS o equivalente, para conformar la clasificacion final en fechas preestablecidas. II. Sera responsable del respetar los horarios y calendario de trabajo comprometidos con el tesista, incluyendo la revision detallada del texto de la tesis. III. En caso de incumplimiento del tesista lo reportara a la Secretaria Academica para deslindar responsabilidades.


Documento: 10006
Articulo: 10065
Capitulo: Del Director de Tesis.

El Director de tesis podra formar parte del jurado examinador, pero no podra desempenar el cargo de presidente del mismo, sino que actuara como vocal.


Documento: 10006
Articulo: 10066
Capitulo: Del Codirector.

En el caso de que se haga necesario que una persona participe en la codireccion de la tesis, la Secretaria Academica estudiara, y en su caso avalara la participacion de la misma. Su participacion sera considerada como de "codireccion" de la tesis.


Documento: 10006
Articulo: 10067
Capitulo: Del Codirector.

La propuesta sobre la participacion de un codirector la debera presentar por escrito el propio estudiante. En el caso de que se trate de una persona ajena a la Universidad Autonoma de Entre Rios debera anexar una copia de su curriculum.


Documento: 10006
Articulo: 10068
Capitulo: Del Codirector.

Una consideracion sobre la justificacion de la codireccion se hara cuando la naturaleza de la tesis, el contenido de la misma, o la metodologia de investigacion particular, no pueda ser cubierta apropiadamente por los profesores de tiempo completo o medio tiempo de un solo departamento.


Documento: 10006
Articulo: 10069
Capitulo: De los Asesores.

La funcion de los asesores de tesis sera la de contribuir al desarrollo del proyecto de tesis en aspectos especificos de contenido, metodologico y estadistico, entre otros, es decir, complementando y enriqueciendo aspectos concretos.


Documento: 10006
Articulo: 10070
Capitulo: De los Asesores.

Podran fungir como asesores de tesis tanto profesores de tiempo completo, medio tiempo, como de tiempo parcial.


Documento: 10006
Articulo: 10071
Capitulo: De los Asesores.

Tambien, se podran considerar como asesores de tesis a personas externas a la institucion, sin embargo, su participacion debe haber sido avalada por la Secretaria Academica y aprobada por el Consejo Directivo.


Documento: 10006
Articulo: 10072
Capitulo: De los Asesores.

El grado academico o profesional minimo de los asesores de tesis y cualquier otra caracteristica sera establecido por cada Carrera.


Documento: 10006
Articulo: 10073
Capitulo: De la Secretaria Academica.

La Secretaria Academica es la responsable de administrar el proceso de tesis para los alumnos inscriptos en las asignaturas pertienentes y/o candidatos al grado en proceso de titulacion.


Documento: 10006
Articulo: 10074
Capitulo: De la Secretaria Academica.

La Secretaria Academica tendra al menos las siguientes funciones y responsabilidades: I. Al inicio del ano academico, elaborara y publicara un programa o calendario de actividades para normar los procesos de elaboracion y defensa de las tesis. II. Vigilara que una copia del "Reglamento" de tesis vigente este disponible en reserva en la Biblioteca, otra en el departamento y que un archivo electronico que contenga ese reglamento este disponible en el sistema de informacion de electronica que posee la Universidad Autonoma de Entre Rios. III. Convocara al titular de TESIS o equivalente a las juntas regulares de revision de propuestas de tesis. IV. Acordara con el Consejo Directivo la composicion de los jurados para examenes y las fechas de los mismos. V. Llevara un archivo o registro de todo lo concerniente a los proyectos de tesis. VI. Sera el encargado de velar por el aprovisionamiento o gestionar los apoyos institucionales necesarios para conseguir equipo, materiales y recursos para proyectos. VII. Exigira una carta de compromiso, cuando el proyecto implique ayuda financiera o tecnica de organismos externos para que la propuesta sea aprobada. VIII. De comun acuerdo con los directores de tesis revisara que los examinados hayan cumplido con realizar las correcciones finales a su tesis, presentar el o los ejemplares requeridos y que satisfaga los requerimientos fijados por otras instancias universitarias para graduacion.


Documento: 10006
Articulo: 10075
Capitulo: Capitulo V. Del Formato y Organizacion de la Tesis.

El nombre y contenidos especificos de cada capitulo sera determinado conjuntamente por el tesista y su Director, pero su contenido nunca podra ser inferior a lo senalado en el proyecto aprobado.


Documento: 10006
Articulo: 10076
Capitulo: Capitulo V. Del Formato y Organizacion de la Tesis.

De acuerdo al articulo anterior, la tesis podra adoptar el capitulado que se considere mas adecuado para la tematica cubierta pero debera estar acorde a las normas minimas fijadas por el Consejo Academico. En caso de no existir norma departamental o de carrera especifica, seguira el criterio de garantizar el que la tesis contenga al menos, tres capitulos o bloques de conceptos, que cubran: I. Una introduccion general que, entro otros aspectos, debera plantear el problema o proposito del trabajo. II. Una revision de la literatura o analisis de los antecedentes, trabajos previos, teoria relevante, o investigaciones relacionadas. III. Conclusiones del trabajo en terminos del objetivo o los propositos originales.


Documento: 10006
Articulo: 10077
Capitulo: Capitulo VI. Sobre la Presentacion Final de la Tesis.

Para la presentacion de la tesis deben tenerse en cuenta las siguientes normas establecidas por la Universidad: Los trabajos de tesis deben contener como minimo las siguientes secciones: Caratula: Titulo, nombre del Director, nombre de los integrantes del proyecto. Resumen: Deber incluir un resumen en Castellano e Ingles no mas de 200 palabras en donde se exponga con claridad los objetivos y los alcances del trabajo. Introduccion: Breve referencia del trabajo mencionando la parte novedosa del trabajo. Desarrollo: Descripcion del trabajo. Conclusiones: Alcances de los resutados obtenidos, ventajas y desventajas, futuros trabajos, etc. Bibliografia: Las citas bibliograficas deberan ser adecuadas al tema y usando el siguiente formato por orden alfabetico: [AUT/ZZ] Autores, titulo, Puublicacion, Editorial, Ano.


Documento: 10006
Articulo: 10078
Capitulo: Sobre el Jurado.

El jurado de la tesis esta compuesto por el director y otros 2 miembros. El director de tesis debera acordar con el titular de la Catedra TESIS quienes seran los miembros del jurado, al menos uno de ellos del area del tema de la tesis. Ademas sera el responsable conjuntamente con los alumnos de hacerle llegar a cada uno de ellos una copia del trabajo. Cada una debe incluir copia del programa desarrollado si corresponde.


Documento: 10006
Articulo: 10079
Capitulo: Sobre el Jurado.

El jurado debera confeccionar en el momento de la defensa de la tesis, el acta de examen correspondiente, la cual debe ser entregada a la secrtaria del Dpto. junto con dos copias de la tesis destinadas a la biblioteca (incluyendo los disquetes). En caso de no presentarse las copias, se retendra el acta correspondiente hasta dicha presentacion.


Documento: 10006
Articulo: 10080
Capitulo: Sobre el Jurado.

La fecha de presentacion de la tesis de licenciatura debe ser avisada por e-mail a todos los integrantes de la Carrera (listas de docentes y alumnos) por el director o los alumnos con una semana de anticipacion. La presentacion es publicada. La participacion de los 3 (tres) jurados es obligatoria. Eventualmente se podra reemplazar algun miembro del jurado con el acuerdo de la Secretaria Academica, el titular de la Catedra TESIS o equivalente y la aprobacion del Consejo Directivo.


Documento: 10006
Articulo: 10081
Capitulo: Sobre Los Plazos.

El postulante y el Director de Tesis, cumplidos los requisitos administratidos y academicos contenidos en el presente reglamento, solicitaran a la Secretaria Academica de la respectiva Facultad, dia y hora para el examen de tesis.


Documento: 10006
Articulo: 10082
Capitulo: Sobre Los Plazos.

La fecha para el examen formal, sera acordada por la Secretaria Academica con el Consejo Directivo una vez cumplidos los requisitos establecidos. La misma debera ser fijada en un plazo no mayor a los treinta dias a partir de la fecha de aprobacion en el Consejo Directivo.


Documento: 10006
Articulo: 10083
Capitulo: Sobre Los Plazos.

La tesis debe ser presentada al jurado con una antelacion no menor a 30 dias de la fecha de presentacion. Las eventuales correcciones o cambios en la presentacion conduciran a un nuevo plazo de 30 dias u deberan ser informadas al tesista, al Director de Tesis y a la Secretaria Academica en un plazo no mayor a los 20 dias a partir de la fecha de recepcion de la tesis.


Documento: 10006
Articulo: 10084
Capitulo: Sobre Los Plazos.

El plazo sugerido para la presentacion del trabajo es de 1 (un) ano a partir de la presentacion de la propuesta. Cualquier situacion anormal adentro del proyecto debe ser informada al profesor titular de la Catedra TESIS o equivalente y la Secretaria Academica de la respectiva Facultad.


Documento: 10007
Articulo: 10085
Capitulo: 

Apruebese el Reglamento de Responsable de Carreras y Consejo de Carreras que forma parte de la presente como Anexo Unico.


Documento: 10007
Articulo: 10086
Capitulo: 

Determinese que la primera eleccion de Responsable de Carrera conforme a lo establecido en este reglamento se llevara a cabo durante la primera quincena del mes de noviembre de 2004.


Documento: 10007
Articulo: 10087
Capitulo: 

Determinese que la primera eleccion para los Consejos de Carreras conforme a lo establecido en este reglamento se llevara a cabo durante la segunda quincena del mes de noviembre.


Documento: 10007
Articulo: 10088
Capitulo: 

Registrese, comuniquese a quienes corresponda, notifiquese a la parte interesada y oportunamente archivese.


Documento: 10007
Articulo: 10089
Capitulo: DE LOS RESPONSABLES DE CARRERA

Cada carrera de la Facultad de Ciencia y Tecnologia, dependiente de la Universidad Autonoma de Entre Rios contara con un Responsable de Carrera titular y uno suplente, cuyas funciones y modalidad de eleccion estaran estipuladas por el presente Reglamento.


Documento: 10007
Articulo: 10090
Capitulo: DE LOS RESPONSABLES DE CARRERA

A los efectos de este reglamento se entendera por "carrera" a todas aquellas titulaciones de un mismo campo de conocimiento y/o actividad; razon por la cual, en este caso, una carrera involucra a las titulaciones de tecnicatura, profesorado y licenciatura.


Documento: 10007
Articulo: 10091
Capitulo: DE LOS RESPONSABLES DE CARRERA

En aquellas carreras que se dicten simultaneamente en varias subsedes de la Facultad, se elegira un Responsable titular y uno suplente para cada una de ellas.


Documento: 10007
Articulo: 10092
Capitulo: DE LOS RESPONSABLES DE CARRERA

Academicamente, el Responsable dependera de la Secretaria Academica, debiendo dar cuenta a esta de sus actividades, o en quienes esta Secretaria delegue esta funcion.


Documento: 10007
Articulo: 10093
Capitulo: DE LOS RESPONSABLES DE CARRERA

Para ser electo Responsable de Carrera se requiere poseer titulo afin a la carrera para la que se postula o ser Profesor del area de Sistemas o Computacion en el caso de la carrera de Licenciatura en Sistemas Informaticos; ser profesor titular/adjunto de la misma y poseer una antiguedad minima de 4 (cuatro) anos en ejercicio de la docencia en la carrera, computandose a este efecto, la antiguedad de los docentes en los institutos transferidos.


Documento: 10007
Articulo: 10094
Capitulo: DE LOS RESPONSABLES DE CARRERA

Los Responsables duraran 2 (dos) anos en sus funciones, pudiendo ser reelegidos solo por un nuevo periodo consecutivo.


Documento: 10007
Articulo: 10095
Capitulo: DE LOS RESPONSABLES DE CARRERA

Quien resulte electo para desempenar 1a funcion de Responsable en una de las carreras de la Facultad no podra ocupar identica responsabilidad en otra, aunque esta fuera en caracter de suplente.


Documento: 10007
Articulo: 10096
Capitulo: DE LOS RESPONSABLES DE CARRERA

El Responsable de carrera electo como titular recibira una compensacion economica por su funcion, la cual se remunerara en 6 (seis) horas catedras, no computando las mismas para las situaciones de incompatibilidad previstas en la legislacion vigente, en lo referente a que no seran consideradas como horas al frente de alumnos.


Documento: 10007
Articulo: 10097
Capitulo: DE LOS RESPONSABLES DE CARRERA

La actividad del Responsable suplente es ad-honorem, a menos que se produzca licencia por mas de 30 (treinta) dias del titular o renuncia al cargo, computandose las licencias consecutivas. En estos ultimos casos, el Decano reasignara la compensacion economica al suplente, quien sera designado hasta completar el periodo de los 2 (dos) anos o hasta que el titular se reintegre en sus funciones, segun corresponda.


Documento: 10007
Articulo: 10098
Capitulo: DE LOS RESPONSABLES DE CARRERA

Seran funciones del Responsable: a) Presidir los Consejos de Carrera. b) Participar en el diseno, rediseno y actualizacion del Plan de Estudios de la carrera. c) Colaborar en el proceso de evaluacion institucional. d) Participar en las instancias de concursos que la reglamentacion especifica indique. e) Colaborar con la Secretaria Academica y con el Area Alumnado de la Facultad en la confeccion de los horarios de los profesores de la carrera. f) Observar y comunicar, a la Secretaria Academica de la Facultad, la necesidad de cobertura de catedras a los efectos de lograr una adecuada implementacion de los planes de estudios correspondientes. g) Identificar las areas en que se requiera capacitacion para los profesores de la carrera. h) Promover, junto a la Secretaria Academica espacios de intercambio e integracion entre los responsables de otras carreras de la Facultad y de la misma carrera de distintas subsedes. i) Promover la realizacion de proyectos de investigacion y extension, de acuerdo con las lineas previstas por los respectivos Secretarios. j) Velar por le buen funcionamiento de los servicios auxiliares de la docencia, la investigacion y la extension vinculados con la carrera a su cargo (biblioteca, equipamiento informatico, etc.). k) Relevar y proponer la adquisicion de material bibliografico requerido por las catedras e informar de esta situacion a la Secretaria Academica de su dependencia y a traves de esta al Area Biblioteca. l) Propiciar la existencia de ofertas extracurriculares que aborden temas que complementen los incluidos en el plan de estudio de la carrera. m) Participar activamente, en representacion de la Facultad, en las Asociaciones, Federaciones, Redes o Instituciones que hacen al campo de la carrera. n) Elaborar un informe anual de actividades realizadas, el cual debera ser presentado ante la Secretaria Academica y, por intermedio de esta, al Decanato de la Facultad. En dicho informe, ademas, se debera dar cuenta de la planificacion proyectada para el ano siguiente, incluyendo un diagnostico de necesidades, prioridades y requerimientos presupuestarios; previa vista del Consejo de Carrera.


Documento: 10007
Articulo: 10099
Capitulo: DE LOS RESPONSABLES DE CARRERA

El Responsable de carrera sera elegido por sus pares en eleccion directa, por simple mayoria de sufragios, pudiendo ser elegido entre todos los docentes de la carrera, que cumplan lo dispuesto en el Articulo 17 del presente Reglamento.


Documento: 10007
Articulo: 10100
Capitulo: DE LOS RESPONSABLES DE CARRERA

La eleccion de los Responsables sera simultanea en todas las carreras de la Facultad, en tiempo a determinar, mediante la convocatoria del Decano.


Documento: 10007
Articulo: 10101
Capitulo: DE LOS RESPONSABLES DE CARRERA

El Consejo Directivo fijara el cronograma electoral que debera incluir fechas para la presentacion de postulaciones, plazo para oficializacion de los postulantes, para impugnaciones y para la resolucion del comicio, fecha de proclamacion y asuncion de los electos, y designara a la Junta Electoral que tendra la responsabilidad para la Sede y para cada Subsede de fiscalizar el normal desarrollo de la eleccion, desde su inicio hasta su finalizacion.


Documento: 10007
Articulo: 10102
Capitulo: DE LOS RESPONSABLES DE CARRERA

La Junta Electoral estara constituida por 3 (tres) docentes titulares y 3 (tres) suplentes de cualquier categoria, con una antiguedad en alguna catedra de la carrera minima de 1 (un) ano, designados por el Decano a propuesta de los representantes docentes del Consejo Directivo. Los docentes que integren la Junta Electoral no podran participar como elegibles en los cargos en disputa.


Documento: 10007
Articulo: 10103
Capitulo: DE LOS RESPONSABLES DE CARRERA

El Departamento Personal de la Facultad confeccionara para cada carrera de cada sede y/o subsede: a) la lista de electores con su correspondiente antiguedad en la Facultad conforme con el Articulo 17 del presente reglamento, b) la lista de elegibles, conforme con el Articulo 5. La Junta Electoral exhibira la convocatoria y los mencionados padrones en los transparentes que la Facultad destine para ello, con una antelacion de 5 (cinco) dias habiles a la fecha fijada para el inicio del acto eleccionario. Cualquier reclamo debera realizarse por escrito una vez de publicado los padrones y hasta 3 (tres) dias habiles anteriores al inicio del acto eleccionario. La Junta Electoral debera expedirse al respecto dentro de los 3 (tres) dias habiles a la presentacion del reclamo.


Documento: 10007
Articulo: 10104
Capitulo: DE LOS RESPONSABLES DE CARRERA

La emision del voto sera secreta, obligatoria y directa.


Documento: 10007
Articulo: 10105
Capitulo: DE LOS RESPONSABLES DE CARRERA

Seran electores aquellos docentes de la carrera a la cual pertenece su catedra, laboratorio y/o proyecto de investigacion y desarrollo, cualquiera sea su categoria y caracter de designacion que tengan como minimo 1 (un) ano de antiguedad en la carrera y subsede correspondiente.


Documento: 10007
Articulo: 10106
Capitulo: DE LOS RESPONSABLES DE CARRERA

Para ser oficializada una postulacion se debera presentar una nota dirigida a la Junta Electoral, manifestando las aspiraciones al cargo, el nombre del candidato suplente y una nomina firmada por no menos del 15 % del total de electores que avalen la candidatura.


Documento: 10007
Articulo: 10107
Capitulo: DE LOS RESPONSABLES DE CARRERA

La presentacion a la que alude el articulo anterior debe realizarse 5 (cinco) dias habiles previos a la eleccion. Vencido el plazo de 48 horas de la presentacion y no habiendose expedido la Junta, se dara por oficializada la candidatura. Si dentro del plazo previsto mediare alguna observacion, el postulante sera informado de la misma a fin de que subsane el inconveniente, lo cual debera realizarse en el termino de las 24 horas siguientes.


Documento: 10007
Articulo: 10108
Capitulo: DE LOS RESPONSABLES DE CARRERA

La emision de votos se realizara durante 5 (cinco) dias habiles corridos en los horarios establecidos por la Junta Electoral para cada acto eleccionario. A tal fin se habilitara: a) una urna por cada carrera en cada sede o subsede y designara 1 (un) responsable del acto electoral por cada una; b) una copia del padron de electores de cada carrera en cada sede o subsede para la firma del votante despues de haber emitido su voto. En el mismo se hara entrega al votante de una constancia que acredite dicho acto.


Documento: 10007
Articulo: 10109
Capitulo: DE LOS RESPONSABLES DE CARRERA

Para la emision del voto el sufragante debera presentar Documento de Identidad, Libreta Civica, de Enrolamiento o Cedula. Cuando no se pueda establecer inequivocamente la identidad del elector no se estara en condiciones de emitir el voto.


Documento: 10007
Articulo: 10110
Capitulo: DE LOS RESPONSABLES DE CARRERA

Seran pasibles de sancion, aquellos electores que no voten sin justificacion fundada por escrito. A los efectos de dar una efectiva justificacion, debera ser dirigida a la Junta Electoral en el plazo de 30 (treinta) dias habiles a contar a partir del cierre del acto eleccionario.


Documento: 10007
Articulo: 10111
Capitulo: DE LOS RESPONSABLES DE CARRERA

El escrutinio se realizara inmediatamente de concluido el acto eleccionario. Estara presidido por 1 (un) integrante de la Junta Electoral y 1 (un) representante del Decanato pudiendo estar presente como minimo 1 (un) representante de cada carrera, el cual debera ser integrante del padron electoral de la misma. Esta comision labrara un acta con el resultado del escrutinio definitivo y la nomina de los electores que no emitieron su voto junto con toda la documentacion pertinente que se haya generado. Dicha documentacion se elevara al Decano, para su tratamiento en el Consejo Directivo, en la primera reunion posterior al cierre del acto eleccionario. El plazo de impugnaciones y/o reclamos con relacion al acto eleccionario sera de 3 (tres) dias habiles posteriores al cierre del mismo.


Documento: 10007
Articulo: 10112
Capitulo: DE LOS RESPONSABLES DE CARRERA

En caso de empate se realizara una segunda votacion la cual se desarrollara en 1 (un) solo dia dentro de los 5 (cinco) dias habiles siguientes con las mismas exigencias y procedimientos establecidos para la primera votacion.


Documento: 10007
Articulo: 10113
Capitulo: DE LOS RESPONSABLES DE CARRERA

Las actuaciones, deliberaciones y resoluciones de la Junta Electoral deberan constar en Actas debidamente foliadas y firmadas por sus miembros. Esta documentacion, una vez finalizado el comicio, sera archivada por la Secretaria Academica.


Documento: 10007
Articulo: 10114
Capitulo: DE LOS RESPONSABLES DE CARRERA

Cualquier aspecto no previsto en este Reglamento sera resuelto por el Decano, quien podra dar curso y decision a los miembros de la Junta Electoral.


Documento: 10007
Articulo: 10116
Capitulo: DE LOS CONSEJOS DE CARRERA

Los Consejos de Carrera son ambitos de discusion, reflexion y participacion, los cuales estaran integrados con voz y voto por representantes del Claustro docente, estudiantil y graduados, debiendo estos ser elegidos por sus estamentos, estaran conformados por 2 (dos) docentes, 1 (un) alumno y 1 (un) graduado. Dichos consejos deberan constituirse dentro del primer ano de mandato del Responsable electo.


Documento: 10007
Articulo: 10117
Capitulo: DE LOS CONSEJOS DE CARRERA

Seran presididos por el Responsable de carrera quien tendra voz y voto, y en caso de empate su voto se computara doble.


Documento: 10007
Articulo: 10118
Capitulo: DE LOS CONSEJOS DE CARRERA

Seran funciones de los Consejos de Carreras: a) Participar en la evaluacion del proceso de implementacion del plan de estudios de la carrera y proponer, cuando resulte necesario, la actualizacion del mismo. b) Propiciar espacios de reflexion entre docentes, estudiantes, graduados, personal administrativo y autoridades de la carrera a los efectos de elaborar propuestas inherentes a la adecuada implementacion del plan de estudio de la carrera respectiva. c) Sugerir criterios para la reubicacion de docentes o en su defecto para que se proceda a la convocatoria a concursos, segun la reglamentacion vigente. d) Atender los problemas que se originen en la reubicacion de docentes, como primera instancia de apelacion. d) Proponer normativa academica para la carrera. e) Proponer a las autoridades la realizacion de convenios con organizaciones publicas, privadas y de la sociedad civil, cuya vinculacion institucional resulte de interes para la carrera correspondiente. f) Proponer la adquisicion de insumos y otros recursos destinados a la ensenanza. g) Proponer acciones tendientes a fortalecer la insercion de la carrera en el medio social. h) Propiciar la existencia de ofertas extracurriculares que aborden temas que complementen los incluidos en el plan de estudios de la carrera. i) Proponer e incentivar lineas prioritarias en actividades de Extension e Investigacion.


Documento: 10007
Articulo: 10119
Capitulo: DE LOS CONSEJOS DE CARRERA

Los docentes integrantes del consejo de carrera seran elegidos por sus pares de la carrera respectiva, en eleccion directa, por simple mayoria de sufragios. En caso de empate se realizara una nueva eleccion entre los postulantes que hubieran obtenido mayor numero de votos hasta obtener la mayoria necesaria.


Documento: 10007
Articulo: 10120
Capitulo: DE LOS CONSEJOS DE CARRERA

Para ser electo como representantes docentes en el consejo de carrera y para ser electos de los mismos se requiere cumplir las condiciones fijadas en el articulo 17o del presente.


Documento: 10007
Articulo: 10121
Capitulo: DE LOS CONSEJOS DE CARRERA. Disposiciones transitorias

Los representantes del Consejo de carrera duraran 2 (dos) anos en sus funciones y desempenaran las mismas ad-honorem.


Documento: 10007
Articulo: 10122
Capitulo: DE LOS CONSEJOS DE CARRERA. Disposiciones transitorias

Por esta unica vez y hasta tanto se normalice la Facultad, para ser elegido Responsable de Carrera se considerara a todos los docentes que a la fecha de la transferencia a la Universidad, se hayan desempenado como profesor Responsable, Asociado o hayan estado a cargo de una catedra en lugar del requisito establecido en el Articulo 5 de ser profesor titular/adjunto.


Documento: 10007
Articulo: 10123
Capitulo: DE LOS CONSEJOS DE CARRERA. Disposiciones transitorias

Por esta unica vez, y hasta tanto no haya graduados de las distintas carreras, el consejo de carreras se conformara sin este estamento, a partir de la existencia de la misma, seran automaticamente incorporados segun las pautas previstas en el presente.


Documento: 10008
Articulo: 10124
Capitulo: 

Incorporase al articulo 2o de la Ley 24.521 el texto que a continuacion se transcribe, el cual quedara redactado de la siguiente manera: Articulo 2o: El Estado, al que le cabe responsabilidad indelegable en la prestacion del servicio de educacion superior de caracter publico, reconoce y garantiza el derecho a cumplir con ese nivel de la ensenanza a todos aquellos que quieran hacerlo y cuenten con la formacion y capacidad requeridas. Y debera garantizar asimismo la accesibilidad al medio fisico, servicios de interpretacion y los apoyos tecnicos necesarios y suficientes, para las personas con discapacidad.


Documento: 10008
Articulo: 10125
Capitulo: 

Incorporase el inciso f) del articulo 13 de la Ley 24.521, Ley de Educacion Superior, el cual quedara redactado de la siguiente manera: Articulo 13: Los estudiantes de las instituciones estatales de educacion superior tienen derecho: f) Las personas con discapacidad, durante las evaluaciones, deberan contar con los servicios de interpretacion y los apoyos tecnicos necesarios y suficientes.


Documento: 10008
Articulo: 10126
Capitulo: 

Modificase el articulo 28 inciso a) de la Ley 24.521, Ley de Educacion Superior, el cual quedara redactado de la siguiente manera: a) Formar y capacitar cientificos, profesionales, docentes y tecnicos, capaces de actuar con solidez profesional, responsabilidad, espiritu critico y reflexivo, mentalidad creadora, sentido etico y sensibilidad social, atendiendo a las demandas individuales, en particular de las personas con discapacidad, desventaja o marginalidad, y a los requerimientos nacionales y regionales.


Documento: 10008
Articulo: 10127
Capitulo: 

Incorporase al inciso e) del articulo 29 de la Ley 24.521 el texto que a continuacion se transcribe, el cual quedara redactado de la siguiente manera: Articulo 29: Las instituciones universitarias tendran autonomia academica e institucional, que comprende basicamente las siguientes atribuciones: e) Formular y desarrollar planes de estudio, de investigacion cientifica y de extension y servicios a la comunidad incluyendo la ensenanza de la etica profesional y la formacion y capacitacion sobre la problematica de la discapacidad.


Documento: 10008
Articulo: 10128
Capitulo: 

Comuniquese al Poder Ejecutivo. DADA EN LA SALA DE SESIONES DEL CONGRESO ARGENTINO, EN BUENOS AIRES, A LOS ONCE DIAS DEL MES DE ABRIL DEL ANO DOS MIL DOS.  REGISTRADA BAJO EL No 25.573  EDUARDO O. CAMANO.  MARCELO E. LOPEZ ARIAS.  Eduardo D. Rollano.  Juan C. Oyarzun.EDUCACION Ley No 24.195 Ley Federal de Educacion. Derechos, Obligaciones y Garantias. Principios Generales. Politica Educativa. Sistema Educativo Nacional. Estructura del Sistema Educativo Nacional. Descripcion General. Educacion Inicial, Educacion General Basica. Educacion Polimodal. Educacion Superior. Educacion Cuaternaria. Regimenes Especiales. Educacion no Formal. Ensenanza de Gestion Privada. Gratuidad y Asistencialidad. Unidad Escolar y Comunidad Educativa. Derechos yDeberes de los Miembros de la Comunidad Educativa. Calidad de la Educacion y su Evolucion. Gobierno y Administracion. Financiamiento. Disposiciones Transitorias y Complementarias. Sancionada: Abril 14 de 1993. Promulgada: Abril 29 de 1993 El Senado y Camara de Diputados de la Nacion Argentina reunidos en Congreso, etc. sanciona con fuerza de Ley.


Documento: 10008
Articulo: 10129
Capitulo: TITULO I: DERECHOS, OBLIGACIONES Y GARANTIAS

El derecho constitucional de ensenar y aprender queda regulado, para su ejercicio en todo el territorio argentino, por la presente ley que, sobre la base de principios, establece los objetivos de la educacion en tanto bien social y responsabilidad comun, instituye las normas referentes a la organizacion y unidad del Sistema Nacional de Educacion, y senala el inicio y la direccion de su paulatina reconvencion para la continua adecuacion a las necesidades nacionales dentro de los procesos de integracion.


Documento: 10008
Articulo: 10130
Capitulo: TITULO I: DERECHOS, OBLIGACIONES Y GARANTIAS

El Estado nacional tiene la responsabilidad principal e indelegable de fijar y controlar el cumplimiento de la politica educativa, tendiente a conformar una sociedad argentina justa y autonoma, a la vez que integrada a la region, al continente y al mundo.


Documento: 10008
Articulo: 10131
Capitulo: TITULO I: DERECHOS, OBLIGACIONES Y GARANTIAS

El Estado nacional, las provincias y la Municipalidad de la Ciudad de Buenos Aires, garantizan el acceso a la educacion en todos los ciclos, niveles y regimenes especiales, a toda la poblacion, mediante la creacion, sostenimiento, autorizacion y supervision de los servicios necesarios, con la participacion de la familia, la comunidad, sus organizaciones y la iniciativa privada.


Documento: 10008
Articulo: 10132
Capitulo: TITULO I: DERECHOS, OBLIGACIONES Y GARANTIAS

Las acciones educativas son responsabilidad de la familia, como agente natural y primario de la educacion, del Estado nacional como responsable principal, de las provincias, los municipios, la Iglesia Catolica, las demas confesiones religiosas oficialmente reconocidas y las organizaciones sociales.


Documento: 10008
Articulo: 10133
Capitulo: TITULO II: PRINCIPIOS GENERALES. CAPITULO I: DE LA POLITICA EDUCATIVA

El Estado nacional debera fijar los lineamientos de la politica educativa respetando los siguientes derechos, principios y criterios: a) El fortalecimiento de la identidad nacional atendiendo a las idiosincrasias locales, provinciales y regionales. b) El afianzamiento de la soberania de la Nacion. c) La consolidacion de la democracia en su forma representativa, republicana y federal. d) El desarrollo social, cultural, cientifico, tecnologico y el crecimiento economico del pais. e) La libertad de ensenar y aprender. f) La concrecion de una efectiva igualdad de oportunidades y posibilidades para todos los habitantes y el rechazo a todo tipo de discriminacion. g) La equidad a traves de la justa distribucion de los servicios educacionales a fin de lograr la mejor calidad posible y resultados equivalentes a partir de la heterogeneidad de la poblacion. h) La cobertura asistencial y la elaboracion de programas especiales para posibilitar el acceso, permanencia y egreso de todos los habitantes al sistema educativo propuesto por la presente ley. i) La educacion concebida como proceso permanente. j) La valorizacion del trabajo como realizacion del hombre y de la sociedad y como eje vertebrador del proceso social y educativo. k) La integracion de las personas con necesidades especiales mediante el pleno desarrollo de sus capacidades. l) El desarrollo de una conciencia sobre nutricion, salud e higiene, profundizando su conocimiento y cuidado como forma de prevencion de las enfermedades y de las dependencias psicofisicas. ll) El fomento de las actividades fisicas y deportivas para posibilitar el desarrollo armonico e integral de las personas. m) La conservacion del medio ambiente, teniendo en cuenta las necesidades del ser humano como integrante del mismo. n) La superacion de todo estereotipo discriminatorio en los materiales didacticos. n) La erradicacion del analfabetismo mediante la educacion de los jovenes y adultos que no hubieran completado la escolaridad obligatoria. o) La armonizacion de las acciones educativas formales como la actividad no formal ofrecida por los diversos sectores de la sociedad y las modalidades informales que surgen espontaneamente en ella. p) El estimulo, promocion y apoyo a las innovaciones educativas y a los regimenes alternativos de educacion, particularmente los sistemas abiertos y a distancia. q) El derecho de las comunidades aborigenes a preservar sus pautas culturales y al aprendizaje y ensenanza de su lengua, dando lugar a la participacion de sus mayores en el proceso de ensenanza. r) El establecimiento de las condiciones que posibiliten el aprendizaje de conductas de convivencia social pluralista y participativa. s) La participacion de la familia, la comunidad, las asociaciones docentes legalmente reconocidas y las organizaciones sociales. t) El derecho de los padres como integrantes de la comunidad educativa a asociarse y a participar en organizaciones de apoyo a la gestion educativa. u) El derecho de los alumnos a que se respete su integridad, dignidad, libertad de conciencia, de expresion y a recibir orientacion. v) El derecho de los docentes universitarios a la libertad de catedra y de todos los docentes a la dignificacion y jerarquizacion de su profesion. w) La participacion del Congreso de la Nacion segun lo establecido en el articulo 53, inciso n).


Documento: 10008
Articulo: 10134
Capitulo: TITULO II: PRINCIPIOS GENERALES. CAPITULO II: DEL SISTEMA EDUCATIVO NACIONAL

El sistema educativo posibilitara la formacion integral y permanente del hombre y la mujer, con vocacion nacional, proyeccion regional y continental y vision universal, que se realicen como personas en las dimensiones cultural, social, estetica, etica y religiosa, acorde con sus capacidades, guiados por los valores de vida, libertad, bien, verdad, paz, solidaridad, tolerancia, igualdad y justicia. Capaces de elaborar, por decision existencial, su propio proyecto de vida. Ciudadanos responsables, protagonistas criticos, creadores y transformadores de la sociedad, a traves del amor, el conocimiento y el trabajo. Defensores de las instituciones democraticas y del medio ambiente.


Documento: 10008
Articulo: 10135
Capitulo: TITULO II: PRINCIPIOS GENERALES. CAPITULO II: DEL SISTEMA EDUCATIVO NACIONAL

El sistema educativo esta integrado por los servicios educativos de las jurisdicciones nacional, provincial y municipal, que incluyen los de las entidades de gestion privada reconocidas.


Documento: 10008
Articulo: 10136
Capitulo: TITULO II: PRINCIPIOS GENERALES. CAPITULO II: DEL SISTEMA EDUCATIVO NACIONAL

El sistema educativo asegurara a todos los habitantes del pais el ejercicio efectivo de su derecho a aprender, mediante la igualdad de oportunidades y posibilidades, sin discriminacion alguna.


Documento: 10008
Articulo: 10137
Capitulo: TITULO II: PRINCIPIOS GENERALES. CAPITULO II: DEL SISTEMA EDUCATIVO NACIONAL

El sistema educativo ha de ser flexible, articulado, equitativo, abierto, prospectivo y orientado a satisfacer las necesidades nacionales y la diversidad regional.


Documento: 10008
Articulo: 10138
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO I: DESCRIPCION GENERAL

La estructura de sistema educativo, que sera implementada en forma gradual y progresiva, estara integrada por: a) Educacion Inicial, constituida por el jardin de infantes para ninos/as de 3 a 5 anos de edad, siendo obligatorio el ultimo ano. Las provincias y la Municipalidad de la Ciudad de Buenos Aires estableceran, cuando sea necesario, servicios de jardin maternal para ninos/as menores de 3 anos y prestaran apoyo a las instituciones de la comunidad para que estas los brinden y ayuda a las familias que los requieran. b) Educacion General Basica, obligatoria, de 9 anos de duracion a partir de los 6 anos de edad, entendida como una unidad pedagogica integral y organizada en ciclos, segun lo establecido en el articulo 15. c) Educacion Polimodal, despues del cumplimiento de la Educacion General Basica, impartida por instituciones especificas de tres anos de duracion como minimo. d) Educacion Superior, profesional y academica de grado, luego de cumplida la Educacion Polimodal; su duracion sera determinada por las instituciones universitarias y no universitarias, segun corresponda. e) Educacion de Posgrado. (Expresion "cuaternaria" sustituida por expresion "de posgrado" por art. 86, inc. a) de la Ley No 24.521 B.O. 10/08/1995)


Documento: 10008
Articulo: 10139
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO I: DESCRIPCION GENERAL

El sistema educativo comprende, tambien, otros regimenes especiales que tienen por finalidad atender las necesidades que no pudieran ser satisfechas por la estructura basica, y que exijan ofertas especificas diferenciadas en funcion de las particularidades o necesidades del educando o del medio. Las provincias y la Municipalidad de la Ciudad de Buenos Aires acordaran en el seno del Consejo Federal de Cultura y Educacion, ofertas educativas de menor duracion y con preparacion ocupacional especifica, para quienes hayan terminado la Educacion General Basica y obligatoria. Ello no impedira a los educandos proseguir estudios en los siguientes niveles del sistema.


Documento: 10008
Articulo: 10140
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO I: DESCRIPCION GENERAL

Los niveles, ciclos y regimenes especiales que integren la estructura del sistema educativo deben articularse, a fin de profundizar los objetivos, facilitar el pasaje y continuidad, y asegurar la movilidad horizontal y vertical de los alumnos/as. En casos excepcionales, el acceso a cada uno de ellos no exigira el cumplimiento cronologico de los anteriores sino la acreditacion, mediante evaluacion por un jurado de reconocida competencia, de las aptitudes y conocimientos requeridos.


Documento: 10008
Articulo: 10141
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO II: EDUCACION INICIAL

Los objetivos de la Educacion Inicial son: a) Incentivar el proceso de estructuracion del pensamiento, de la imaginacion creadora, las formas de expresion personal y de comunicacion verbal y grafica. b) Favorecer el proceso de maduracion del nino/a en lo sensorio motor, la manifestacion ludica y estetica, la iniciacion deportiva y artistica, el crecimiento socio-afectivo, y los valores eticos. c) Estimular habitos de integracion social, de convivencia grupal, de solidaridad y cooperacion y de conservacion del medio ambiente. d) Fortalecer la vinculacion entre la institucion educativa y la familia. e) Prevenir y atender las desigualdades fisicas, psiquicas y sociales originadas en deficiencias de orden biologico, nutricional, familiar y ambiental mediante programas especiales y acciones articuladas con otras instituciones comunitarias.


Documento: 10008
Articulo: 10142
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO II: EDUCACION INICIAL

Todos los establecimientos que presten este servicio, sean de gestion estatal o privada, seran autorizados y supervisados por las autoridades educativas de las provincias y la Municipalidad de la Ciudad de Buenos Aires. Esto sera extensivo a las actividades pedagogicas dirigidas a ninos/as menores de 3 anos, las que deberan estar a cargo de personal docente especializado.


Documento: 10008
Articulo: 10143
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO III: EDUCACION GENERAL BASICA

Los objetivos de la Educacion General Basica son: a) Proporcionar una formacion basica comun a todos los ninos y adolescentes del pais garantizando su acceso, permanencia y promocion y la igualdad en la calidad y logros de los aprendizajes. b) Favorecer el desarrollo individual, social y personal para un desempeno responsable, comprometido con la comunidad, consciente de sus deberes y derechos, y respetuoso de los demas. c) Incentivar la busqueda permanente de la verdad, desarrollar el juicio critico y habitos valorativos y favorecer el desarrollo de las capacidades fisicas, intelectuales, afectivovolitivas, esteticas y los valores eticos y espirituales. d) Lograr la adquisicion y el dominio instrumental de los saberes considerados socialmente significativos: comunicacion verbal y escrita, lenguaje y operatoria matematica, ciencias naturales y ecologia, ciencias exactas, tecnologia e informatica, ciencias sociales y cultura nacional, latinoamericana y universal.e) Incorporar el trabajo como metodologia pedagogica, en tanto sintesis entre teoria y practica, que fomenta la reflexion sobre la realidad, estimula el juicio critico y es medio de organizacion y promocion comunitaria. f) Adquirir habitos de higiene y de preservacion de la salud en todas sus dimensiones. g) Utilizar la educacion fisica y el deporte como elemento indispensable para desarrollar con integralidad la dimension psicofisica. h) Conocer y valorar criticamente nuestra tradicion y patrimonio cultural, para poder optar por aquellos elementos que mejor favorezcan el desarrollo integral como persona.


Documento: 10008
Articulo: 10144
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO IV: EDUCACION POLIMODAL

Los objetivos del ciclo Polimodal son: a) Preparar para el ejercicio de los derechos y el cumplimiento de los deberes de ciudadano/a en una sociedad democratica moderna, de manera de lograr una voluntad comprometida con el bien comun, para el uso responsable de la libertad y para la adopcion de comportamientos sociales de contenido etico en el plano individual, familiar, laboral y comunitario. b) Afianzar la conciencia del deber de constituirse en agente de cambio positivo en su medio social y natural. c) Profundizar el conocimiento teorico en un conjunto de saberes agrupados segun las orientaciones siguientes: humanistica, social, cientifica y tecnica. d) Desarrollar habilidades instrumentales, incorporando el trabajo como elemento pedagogico, que acrediten para el acceso a los sectores de la produccion y del trabajo. e) Desarrollar una actitud reflexiva y critica ante los mensajes de los medios de comunicacion social. f) Favorecer la autonomia intelectual y el desarrollo de las capacidades necesarias para la prosecucion de estudios ulteriores. g) Propiciar la practica de la educacion fisica y del deporte, para posibilitar el desarrollo armonico e integral del/la joven y favorecer la preservacion de su salud psicofisica.


Documento: 10008
Articulo: 10145
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO IV: EDUCACION POLIMODAL

La organizacion del ciclo Polimodal incorporara con los debidos recaudos pedagogicos y sociales, el regimen de alternancia entre la institucion escolar y las empresas. Se procurara que las organizaciones empresarias y sindicales asuman un compromiso efectivo en el proceso de formacion, aportando sus iniciativas pedagogicas, los espacios adecuados y el acceso a la tecnologia del mundo del trabajo y la produccion.


Documento: 10008
Articulo: 10146
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

La etapa profesional de grado no universitario se cumplira en los institutos de formacion docente o equivalentes y en institutos de formacion tecnica que otorgaran titulos profesionales y estaran articulados horizontal y verticalmente con la universidad.


Documento: 10008
Articulo: 10147
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

Los objetivos de la formacion docente son: a) Preparar y capacitar para un eficaz desempeno en cada uno de los niveles del sistema educacional y en las modalidades mencionadas posteriormente en esta ley. b) Perfeccionar, con criterio permanente a graduados y docentes en actividad en los aspectos cientifico, metodologico, artistico y cultural. Formar investigadores y administradores educativos. c) Formar al docente como elemento activo de participacion en el sistema democratico. d) Fomentar el sentido responsable de ejercicio de la docencia y el respeto por la tarea educadora.


Documento: 10008
Articulo: 10148
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

Los institutos de formacion tecnica tendran como objetivo el de brindar formacion profesional y reconvencion permanente en las diferentes areas del saber tecnico y practico de acuerdo con los intereses de los alumnos y la actual y potencial estructura ocupacional.


Documento: 10008
Articulo: 10149
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

La etapa profesional y academica de grado universitario se cumplira en instituciones universitarias entendidas como comunidades de trabajo que tienen la finalidad de ensenar, realizar investigacion, construir y difundir conocimientos, promover la cultura nacional, producir bienes y prestar servicios con proyeccion social y contribuir a la solucion de los problemas argentinos y continentales.


Documento: 10008
Articulo: 10150
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

Son funciones de las universidades: a) Formar y capacitar tecnicos y profesionales, conforme a los requerimientos nacionales y regionales, atendiendo las vocaciones personales y recurriendo a los adelantos mundiales de las ciencias, las artes y las tecnicas que resulten de interes para el pais. b) Desarrollar el conocimiento en el mas alto nivel con sentido critico, creativo e interdisciplinario, estimulando la permanente busqueda de la verdad. c) Difundir el conocimiento cientifico-tecnologico para contribuir al permanente mejoramiento de las condiciones de vida de nuestro pueblo y de la competitividad tecnologica del pais. d) Estimular una sistematica reflexion intelectual y el estudio de la cultura y la realidad nacional, latinoamericana y universal. e) Ejercer la consultoria de organismos nacionales y privados.


Documento: 10008
Articulo: 10151
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

Las universidades gozan de autonomia academica y autarquia administrativa y economico-financiera en el marco de la legislacion especifica.


Documento: 10008
Articulo: 10152
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO V: EDUCACION SUPERIOR

La organizacion y autorizacion de universidades alternativas, experimentales, de postrado, abiertas, a distancia, institutos universitarios tecnologicos, pedagogicos y otros creados libremente por iniciativa comunitaria, se regira por una ley especifica.


Documento: 10008
Articulo: 10153
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VI: EDUCACION CUATERNARIA

La Educacion de Posgrado estara bajo la responsabilidad de las universidades y de las instituciones academicas, cientificas y profesionales de reconocido nivel, siendo requisito para quienes se inscriban el haber terminado la etapa de grado o acreditar conocimiento y experiencia suficientes para el cursado del mismo. (Expresion "cuaternaria" sustituida por expresion "de posgrado" por art. 86, inc. a) de la Ley No 24.521 B.O. 10/08/1995)


Documento: 10008
Articulo: 10154
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VI: EDUCACION CUATERNARIA

El objetivo de la Educacion de Posgrado es profundizar y actualizar la formacion cultural, docente, cientifica, artistica y tecnologica mediante la investigacion, la reflexion critica sobre la disciplina y el intercambio sobre los avances en las especialidades. (Expresion "cuaternaria" sustituida por expresion "de posgrado" por art. 86, inc. a) de la Ley No 24.521 B.O. 10/08/1995)


Documento: 10008
Articulo: 10156
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. A: EDUCACION ESPECIAL

Las autoridades educativas de las provincias y de la Municipalidad de la Ciudad de Buenos Aires coordinaran con las de otras areas acciones de caracter preventivo y otras dirigidas a la deteccion de ninos/as con necesidades educativas especiales. El cumplimiento de la obligatoriedad indicada en el articulo 10 incisos a) y b), tendra en cuenta las condiciones personales del educando/a.


Documento: 10008
Articulo: 10157
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. A: EDUCACION ESPECIAL

Los objetivos de la Educacion Especial son: a) Garantizar la atencion de las personas con estas necesidades educativas desde el momento de su deteccion. Este servicio se prestara en centros o escuelas de educacion especial. b) Brindar una formacion individualizada, normalizadora e integradora, orientada al desarrollo integral de la persona y a una capacitacion laboral que le permita su incorporacion al mundo del trabajo y la produccion.


Documento: 10008
Articulo: 10158
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. A: EDUCACION ESPECIAL

La situacion de los alumnos/as atendidos en centros o escuelas especiales sera revisada periodicamente por equipos de profesionales, de manera de facilitar, cuando sea posible y de conformidad con ambos padres, la integracion a las unidades escolares comunes. En tal caso el proceso educativo estara a cargo del personal especializado que corresponda y se deberan adoptar criterios particulares de curriculo, organizacion escolar, infraestructura y material didactico.


Documento: 10008
Articulo: 10159
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. B: EDUCACION DE ADULTOS

Los objetivos de la Educacion de Adultos son: a) El desarrollo integral y la calificacion laboral de aquellas personas que no cumplieron con la regularidad de la Educacion General Basica y Obligatoria, o habiendo cumplido con la misma, deseen adquirir o mejorar su preparacion a los efectos de proseguir estudios en los otros niveles del sistema, dentro o fuera de este regimen especial. b) Promover la organizacion de sistemas y programas de formacion y reconvencion laboral, los que seran alternativos y suplementarios a los de la educacion formal. Estos sistemas se organizaran con la participacion concertada de las autoridades laborales, organizaciones sindicales y empresarias y otras organizaciones sociales vinculadas al trabajo y la produccion. c) Brindar la posibilidad de acceder a servicios educativos en los distintos niveles del sistema a las personas que se encuentren privadas de libertad en establecimientos carcelarios, servicios que seran supervisados por las autoridades educativas correspondientes. d) Brindar la posibilidad de alfabetizacion, bajo la supervision de las autoridades educativas oficiales, a quienes se encuentren cumpliendo con el servicio militar obligatorio.


Documento: 10008
Articulo: 10160
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. C: EDUCACION ARTISTICA

Los contenidos de la educacion artistica que se correspondan con los de los ciclos y niveles en los que se basa la estructura del sistema deberan ser equivalentes, diferenciandose unicamente por las disciplinas artisticas y pedagogicas.


Documento: 10008
Articulo: 10161
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. C: EDUCACION ARTISTICA

La docencia de las materias artisticas en el nivel inicial y en la educacion primaria tendra en cuenta las particularidades de la formacion en este regimen especial. Estara a cargo de los maestros egresados de las escuelas de arte que contemplen el requisito de que sus alumnos/as completen la educacion media.


Documento: 10008
Articulo: 10162
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. D: OTROS REGIMENES ESPECIALES

Las autoridades educativas oficiales: a) Organizaran o facilitaran la organizacion de programas a desarrollarse en los establecimientos comunes para la deteccion temprana, la ampliacion de la formacion y el seguimiento de los alumnos/as con capacidades o talentos especiales. b) Promoveran la organizacion y el funcionamiento del sistema de educacion abierta y a distancia y otros regimenes especiales alternativos dirigidos a sectores de la poblacion que no concurran a establecimientos presenciales o que requieran servicios educativos complementarios. A tal fin, se dispondra, entre otros medios, de espacios televisivos y radiales. c) Supervisaran las acciones educativas impartidas a ninos/as y adolescentes que se encuentren internados transitoriamente por circunstancias objetivas de caracter diverso. Estas acciones estaran a cargo del personal docente y se corresponderan con los contenidos curriculares fijados para cada ciclo del sistema educativo. En todos los casos que sea posible, se instrumentaran las medidas necesarias para que estos educandos en situaciones atipicas cursen sus estudios en las escuelas comunes del sistema, con el apoyo de personal docente especializado. d) En todos los casos de regimenes especiales alternativos se asegurara que el proceso de ensenanza-aprendizaje tenga un valor formativo equivalente al logrado en las etapas del sistema formal.


Documento: 10008
Articulo: 10163
Capitulo: TITULO III: ESTRUCTURA DEL SISTEMA EDUCATIVO NACIONAL. CAPITULO VII: REGIMENES ESPECIALES. D: OTROS REGIMENES ESPECIALES

El Estado Nacional promovera programas, en coordinacion con las pertinentes jurisdicciones, de rescate y fortalecimiento de lenguas y culturas indigenas, enfatizando su caracter de instrumentos de integracion.


Documento: 10008
Articulo: 10164
Capitulo: TITULO IV: EDUCACION NO FORMAL

Las autoridades educativas oficiales: a) Promoveran la oferta de servicios de educacion no formal vinculados o no con los servicios de educacion formal. b) Propiciaran acciones de capacitacion docente para esta area. c) Facilitaran a la comunidad informacion sobre la oferta de educacion no formal. d) Promoveran convenios con asociaciones intermedias a los efectos de realizar programas conjuntos de educacion no formal que respondan a las demandas de los sectores que representan. e) Posibilitaran la organizacion de centros culturales para jovenes, quienes participaran en el diseno de su propio programa de actividades vinculadas con el arte, el deporte, la ciencia y la cultura. Estaran a cargo de personal especializado, otorgaran las certificaciones correspondientes y se articularan con el ciclo Polimodal. f) Facilitaran el uso de la infraestructura edilicia y el equipamiento de las instituciones publicas y de los establecimientos del sistema educativo formal, para la educacion no formal sin fines de lucro. g) Protegeran los derechos de los usuarios de los servicios de educacion no formal organizados por instituciones de gestion privada que cuenten con reconocimiento oficial. Aquellos que no tengan este reconocimiento quedaran sujetos a las normas del derecho comun.


Documento: 10008
Articulo: 10165
Capitulo: TITULO V: DE LA ENSENANZA DE GESTION PRIVADA

Los servicios educativos de gestion privada estaran sujetos al reconocimiento previo y a la supervision de las autoridades educativas oficiales. Tendran derecho a prestar estos servicios los siguientes agentes: La Iglesia Catolica y demas confesiones religiosas inscriptas en el Registro Nacional de Cultos; las sociedades, asociaciones, fundaciones y empresas con personeria juridica; y las personas de existencia visible. Estos agentes tendran, dentro del Sistema Nacional de Educacion y con sujecion a las normas reglamentarias, los siguientes derechos y obligaciones: a) Derechos: Crear, organizar y sostener escuelas; nombrar y promover a su personal directivo, docente, administrativo y auxiliar; disponer sobre la utilizacion del edificio escolar; formular planes y programas de estudio; otorgar certificados y titulos reconocidos; participar del planeamiento educativo. b) Obligaciones: Responder a los lineamientos de la politica educativa nacional y jurisdiccional; ofrecer servicios educativos que respondan a necesidades de la comunidad, con posibilidad de abrirse solidariamente a cualquier otro tipo de servicio (recreativo, cultural, asistencial); brindar toda la informacion necesaria para el control pedagogico contable y laboral por parte del Estado.


Documento: 10008
Articulo: 10166
Capitulo: TITULO V: DE LA ENSENANZA DE GESTION PRIVADA

El aporte estatal para atender los salarios docentes de los establecimientos educativos de gestion privada, se basara en criterios objetivos de acuerdo al principio de justicia distributiva en el marco de la justicia social y teniendo en cuenta entre otros aspectos: la funcion social que cumple en su zona de influencia, el tipo de establecimiento y la cuota que se percibe.


Documento: 10008
Articulo: 10167
Capitulo: TITULO V: DE LA ENSENANZA DE GESTION PRIVADA

Los/as docentes de las instituciones educativas de gestion privada reconocidas tendran derecho a una remuneracion minima igual a la de los/as docentes de instituciones de gestion estatal y deberan poseer titulos reconocidos por la normativa vigente en cada jurisdiccion.


Documento: 10008
Articulo: 10168
Capitulo: TITULO VI: GRATUIDAD Y ASISTENCIALIDAD

El Estado nacional, las provincias y la Municipalidad de la Ciudad de Buenos Aires se obligan, mediante la asignacion en los respectivos presupuestoseducativos a garantizar el principio de gratuidad en los servicios estatales, en todos los niveles y regimenes especiales. El Estado nacional realizara el aporte financiero principal al sistema universitario estatal para asegurar que ese servicio se preste a todos los habitantes que lo requieran. Las universidades podran disponer de otras fuentes complementarias de financiamiento que seran establecidas por una ley especifica, sobre la base de los principios de gratuidad y equidad. El Estado nacional, las provincias y la Municipalidad de la Ciudad de Buenos Aires estableceran un sistema de becas para alumnos/as en condiciones socioeconomicas desfavorables, que cursen ciclos y/o niveles posteriores a la Educacion General Basica y Obligatoria, las que se basaran en el rendimiento academico.


Documento: 10008
Articulo: 10169
Capitulo: TITULO VI: GRATUIDAD Y ASISTENCIALIDAD

El Estado nacional, las provincias y la Municipalidad de la Ciudad de Buenos Aires se obligan a: a) Garantizar a todos los alumnos/as el cumplimiento de la obligatoriedad que determina la presente ley, ampliando la oferta de servicios e implementando, con criterio solidario, en concertacion con los organismos de accion social estatales y privados, cooperadoras, cooperativas y otras asociaciones intermedias, programas asistenciales de salud, alimentacion, vestido, material de estudio y transporte para los ninos/as y adolescentes de los sectores sociales mas desfavorecidos. En todos los casos los organismos estatales y privados integraran sus esfuerzos, a fin de lograr la optimizacion de los recursos, y se adoptaran acciones especificas para las personas que no ingresan al sistema, para las que lo abandonan y para las repitentes. b) Organizar planes asistenciales especificos para los ninos/as atendidos por la Educacion Inicial pertenecientes a familias con necesidades basicas insatisfechas, en concertacion con organismos de accion social estatales y privados. c) Organizar planes asistenciales especificos para los ninos/as atendidos por la Educacion Especial pertenecientes a familias con necesidades basicas insatisfechas desde la etapa de estimulacion temprana, en concertacion con los organismos estatales y privados que correspondan. Los planes y programas de salud y alimentacion que se desarrollen en el ambito escolar estaran orientados al conjunto de los alumnos/as.


Documento: 10008
Articulo: 10170
Capitulo: TITULO VII: UNIDAD ESCOLAR Y COMUNIDAD EDUCATIVA

La unidad escolar como estructura pedagogica formal del sistema y como ambito fisico y social adoptara criterios institucionales y practicas educativas democraticas, establecera vinculos con las diferentes organizaciones de su entorno y pondra a disposicion su infraestructura edilicia para el desarrollo de actividades extraescolares y comunitarias preservando lo atinente al destino y funciones especificas del establecimiento.


Documento: 10008
Articulo: 10171
Capitulo: TITULO VII: UNIDAD ESCOLAR Y COMUNIDAD EDUCATIVA

La comunidad educativa estara integrada por directivos, docentes, padres, alumnos/as, ex-alumnos/as, personal administrativo y auxiliar de la docencia y organizaciones representativas, y participara segun su propia opcion y de acuerdo al proyecto institucional especifico en la organizacion y gestion de la unidad escolar, y en todo aquello que haga al apoyo y mejoramiento de la calidad de la educacion, sin afectar el ejercicio de las responsabilidades directivas y docentes.


Documento: 10008
Articulo: 10172
Capitulo: TITULO VIII: DERECHOS Y DEBERES DE LOS MIEMBROS DE LA COMUNIDAD EDUCATIVA. CAPITULO I: DE LOS EDUCANDOS

Los educandos tienen derecho a: a) Recibir educacion en cantidad y calidad tales que posibiliten el desarrollo de sus conocimientos, habilidades y su sentido de responsabilidad y responsabilidad social. b) Ser respetados en su libertad de conciencia, sus convicciones religiosas, morales y politicas en el marco de la convivencia democratica. c) Ser evaluados en sus desempenos y logros, conforme con criterios rigurosa y cientificamente fundados, en todos los niveles, ciclos y regimenes especiales del sistema, e informados al respecto. d) Recibir orientacion vocacional, academica y profesional-ocupacional que posibilite su insercion en el mundo laboral o la prosecucion de otros estudios. e) Integrar centros, asociaciones y clubes de estudiantes u otras organizaciones comunitarias para participar en el funcionamiento de las unidades educativas, con responsabilidades progresivamente mayores, a medida que avance en los niveles del sistema. f) Desarrollar sus aprendizajes en edificios que respondan a normas de seguridad y salubridad que cuenten con instalaciones y equipamiento que aseguren la calidad y la eficacia del servicio educativo. g) Estar amparados por un sistema de seguridad social durante su permanencia en el establecimiento escolar y en aquellas actividades programadas por las autoridades educativas correspondientes.


Documento: 10008
Articulo: 10173
Capitulo: TITULO VIII: DERECHOS Y DEBERES DE LOS MIEMBROS DE LA COMUNIDAD EDUCATIVA. CAPITULO II: DE LOS PADRES

Los padres o tutores de los alumnos/as, tienen derecho a: a) Ser reconocidos como agente natural y primario de la educacion. b) Participar en las actividades de los establecimientos educativos en forma individual o a traves de los organos colegiados representativos de la comunidad educativa. c) Elegir para sus hijos/as o pupilos/as, la institucion educativa cuyo ideario responda a sus convicciones filosoficas, eticas o religiosas. d) Ser informados en forma periodica acerca de la evolucion y evaluacion del proceso educativo de sus hijos/as.


Documento: 10008
Articulo: 10174
Capitulo: TITULO VIII: DERECHOS Y DEBERES DE LOS MIEMBROS DE LA COMUNIDAD EDUCATIVA. CAPITULO II: DE LOS PADRES

Los padres o tutores de los alumnos/as, tienen las siguientes obligaciones: a) Hacer cumplir a sus hijos/as con la Educacion General Basica y Obligatoria (articulo 10) o con la Educacion Especial (articulo 27). b) Seguir y apoyar la evolucion del proceso educativo de sus hijos/as. c) Respetar y hacer respetar a sus hijos/as las normas de convivencia de la unidad educativa.


Documento: 10008
Articulo: 10175
Capitulo: TITULO VIII: DERECHOS Y DEBERES DE LOS MIEMBROS DE LA COMUNIDAD EDUCATIVA. CAPITULO III: DE LOS DOCENTES

Sin perjuicio de los derechos laborales reconocidos por la normativa vigente y la que se establezca a traves de una legislacion especifica, se resguardaran los derechos de todos los trabajadores/as de la educacion del ambito estatal y privado a: a) Ejercer su profesion sobre la base del respeto a la libertad de catedra y a la libertad de ensenanza, en el marco de las normas pedagogicas y curriculares establecidas por la autoridad educativa. b) Ingresar en el sistema mediante un regimen de concursos que garantice la idoneidad profesional y el respeto por las incumbencias profesionales, y ascender en la carrera docente, a partir de sus propios meritos y su actualizacion profesional. c) Percibir una remuneracion justa por sus tareas y capacitacion. d) El cuidado de la salud y la prevencion de enfermedades laborales. e) Ejercer su profesion en edificios que reunan las condiciones de salubridad y seguridad acordes con una adecuada calidad de vida y a disponer en su lugar de trabajo del equipamiento y de los recursos didacticos necesarios. f) El reconocimiento de los servicios prestados y el acceso a beneficios especiales cuando los mismos se realicen en establecimientos de zonas desfavorables o aisladas. g) Un sistema previsional que permita, en el ejercicio profesional, la movilidad entre las distintas jurisdicciones, el reconocimiento de los aportes y la antiguedad acumulada en cualquiera de ellas. h) La participacion gremial. i) La capacitacion, actualizacion y nueva formacion en servicio, para adaptarse a los cambios curriculares requeridos. Los trabajadores de la educacion de establecimientos de gestion privada deberan poseer titulos habilitantes reconocidos por la correspondiente jurisdiccion educativa para el ejercicio de la profesion, en cuyo caso tendran derecho a las condiciones de labor prescriptas en el presente articulo, con excepcion de los incisos a) y b).


Documento: 10008
Articulo: 10176
Capitulo: TITULO VIII: DERECHOS Y DEBERES DE LOS MIEMBROS DE LA COMUNIDAD EDUCATIVA. CAPITULO III: DE LOS DOCENTES

Seran deberes de los trabajadores de la educacion: a) Respetar las normas institucionales de la comunidad educativa que integran. b) Colaborar solidariamente en las actividades de la comunidad educativa. c) Orientar su actuacion en funcion del respeto a la libertad y dignidad del alumno/a como persona. d) Su formacion y actualizacion permanente. e) Afianzar el sentido de la responsabilidad en el ejercicio de la docencia y el respeto por la tarea educadora.


Documento: 10008
Articulo: 10177
Capitulo: TITULO IX: DE LA CALIDAD DE LA EDUCACION Y SU EVALUACION

El Ministerio de Cultura y Educacion de la Nacion, las provincias y la Municipalidad de la Ciudad de Buenos Aires, deberan garantizar la calidad de la formacion impartida en los distintos ciclos, niveles y regimenes especiales mediante la evaluacion permanente del sistema educativo, controlando su adecuacion a lo establecido en esta ley, a las necesidades de la comunidad, a la politica educativa nacional, de cada provincia y de la Municipalidad de la Ciudad de Buenos Aires y a las concertadas en el seno del Consejo Federal de Cultura y Educacion. A ese fin debera convocar junto con el Consejo Federal de Cultura y Educacion a especialistas de reconocida idoneidad e independencia de criterio para desarrollar las investigaciones pertinentes por medio de tecnicas objetivas aceptadas y actualizadas. El Ministerio de Cultura y Educacion debera enviar un informe anual a la Comision de Educacion de ambas Camaras del Congreso de la Nacion donde se detallen los analisis realizados y las conclusiones referidas a los objetivos que se establecen en la presente ley.


Documento: 10008
Articulo: 10178
Capitulo: TITULO IX: DE LA CALIDAD DE LA EDUCACION Y SU EVALUACION

La evaluacion de la calidad en el sistema educativo verificara la adecuacion de los contenidos curriculares de los distintos ciclos, niveles y regimenes especiales a las necesidades sociales y a los requerimientos educativos de la comunidad, asi como el nivel de aprendizaje de los alumnos/as y la calidad de formacion docente.


Documento: 10008
Articulo: 10179
Capitulo: TITULO IX: DE LA CALIDAD DE LA EDUCACION Y SU EVALUACION

Las autoridades educativas de las provincias y de la Municipalidad de la Ciudad de Buenos Aires evaluaran periodicamente la calidad y el funcionamiento del sistema educativo en el ambito de su competencia.


Documento: 10008
Articulo: 10180
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION

El gobierno y administracion del sistema educativo asegurara el efectivo cumplimiento de los principios y objetivos establecidos en esta ley, teniendo en cuenta los criterios de:  unidad nacional;  democratizacion;  descentralizacion y federalizacion;  participacion;  equidad;  intersectorialidad;  articulacion;  transformacion e innovacion.


Documento: 10008
Articulo: 10181
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION

El gobierno y administracion del sistema educativo es una responsabilidad concurrente y concertada del Poder Ejecutivo nacional, de los poderes ejecutivos de las provincias y del de la Municipalidad de la Ciudad de Buenos Aires.


Documento: 10008
Articulo: 10182
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO I: DEL MINISTERIO DE CULTURA Y EDUCACION

El Poder Ejecutivo nacional, a traves del ministerio especifico, debera: a) Garantizar el cumplimiento de los principios, objetivos y funciones del Sistema Nacional de Educacion. b) Establecer en acuerdo con el Consejo Federal de Cultura y Educacion, los objetivos y contenidos basicos comunes de los curriculos de los distintos niveles, ciclos y regimenes especiales de ensenanza -que faciliten la movilidad horizontal y vertical delos alumnos/as- dejando abierto un espacio curricular suficiente para la inclusion de contenidos que respondan a los requerimientos provinciales, municipales, comunitarios y escolares. c) Dictar normas generales sobre equivalencia de titulos y de estudios, estableciendo la validez automatica de los planes concertados en el seno del Consejo Federal de Cultura y Educacion. d) Favorecer una adecuada descentralizacion de los servicios educativos, y brindar a este efecto el apoyo que requieran las provincias y la Municipalidad de la Ciudad de Buenos Aires. e) Implementar programas especiales para garantizar el ingreso, permanencia y egreso de los alumnos/as en todos los ciclos y niveles del sistema educativo nacional, en coordinacion con el Consejo Federal de Cultura y Educacion. f) Desarrollar programas nacionales y federales de cooperacion tecnica y financiera a fin de promover la calidad educativa y alcanzar logros equivalentes, a partir de las heterogeneidades locales, provinciales y regionales. g) Promover y organizar concertadamente en el ambito del Consejo Federal de Cultura y Educacion, una red de formacion, perfeccionamiento y actualizacion del personal docente y no docente del sistema educativo nacional. h) Coordinar y ejecutar programas de investigacion y cooperacion con universidades y organismos nacionales especificos. i) Administrar los servicios educativos propios y los de apoyo y asistencia tecnica al sistema -entre ellos, los de planeamiento y control; evaluacion de calidad; estadistica; investigacion, informacion y documentacion; educacion a distancia, informatica, tecnologia, educacion satelital, radio y television educativas- en coordinacion con las provincias y la Municipalidad de la Ciudad de Buenos Aires. j) Alentar el uso de los medios de comunicacion social estatales y privados para la difusion de programas educativo-culturales que contribuyan a la afirmacion de la identidad nacional y regional. k) Evaluar el funcionamiento del sistema educativo en todas las jurisdicciones, niveles, ciclos y regimenes especiales, a partir del diseno de un sistema de evaluacion y control periodico de la calidad, concertado en el ambito del Consejo Federal de Cultura y Educacion. l) Dictar las normas generales sobre revalidacion de titulos y certificados de estudios en el extranjero. ll) Coordinar y gestionar la cooperacion tecnica y financiera internacional y bilateral. m) Contribuir con asistencia tecnica para la formacion y capacitacion tecnicoprofesional en los distintos niveles del sistema educativo, en funcion de la reconvencion laboral en las empresas industriales, agropecuarias y de servicios. n) Elaborar una memoria anual donde consten los resultados de la evaluacion del sistema educativo, la que sera enviada al Congreso de la Nacion.


Documento: 10008
Articulo: 10183
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO II: DEL CONSEJO FEDERAL DE CULTURA Y EDUCACION

El Consejo Federal de Cultura y Educacion es el ambito de coordinacion y concertacion del Sistema Nacional de Educacion y esta presidido por el ministro nacional del area e integrado por el responsable de la conduccion educativa de cada jurisdiccion y tres representantes del Consejo de Universidades. (Expresion "un representante del Consejo Interuniversitario Nacional" sustituida por expresion "y tres representantes del Consejo de Universidades" por art. 86, inc. b) de la Ley No 24.521 B.O. 10/08/1995)


Documento: 10008
Articulo: 10184
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO II: DEL CONSEJO FEDERAL DE CULTURA Y EDUCACION

La mision del Consejo Federal de Cultura y Educacion es unificar criterios entre las jurisdicciones, cooperar en la consolidacion de la identidad nacional y en que a todos los habitantes del pais se les garantice el derecho constitucional de ensenar y aprender en forma igualitaria y equitativa.


Documento: 10008
Articulo: 10185
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO II: DEL CONSEJO FEDERAL DE CULTURA Y EDUCACION

El Consejo Federal de Cultura y Educacion tiene las funciones establecidas por las normas de su constitucion y cumplira ademas las siguientes: a) Concertar dentro de los lineamientos de la politica educativa nacional los contenidos basicos comunes, los disenos curriculares, las modalidades y las formas de evaluacion de los ciclos, niveles y regimenes especiales que componen el sistema. b) Acordar los mecanismos que viabilicen el reconocimiento y equivalencia de estudios, certificados y titulos de la educacion formal y no formal en las distintas jurisdicciones. c) Acordar los contenidos basicos comunes de la formacion profesional docente y las acreditaciones necesarias para desempenarse como tal en cada ciclo, nivel y regimen especial. d) Acordar las exigencias pedagogicas que se requeriran para el ejercicio de la funcion docente en cada rama artistica en los distintos niveles y regimenes especiales del sistema. e) Promover y difundir proyectos y experiencias innovadoras y organizar el intercambio de funcionarios, especialistas y docentes mediante convenios, la constitucion de equipos tecnicos interjurisdiccionales y acciones en comun, tendientes a lograr un efectivo aprovechamiento del potencial humano y de los recursos tecnologicos disponibles en el sistema educativo nacional. f) Considerar y proponer orientaciones que tiendan a la preservacion y desarrollo de la cultura nacional en sus diversas manifestaciones, mediante la articulacion de las politicas culturales con el sistema educativo en todos sus niveles y regimenes especiales. g) Garantizar la participacion en el planeamiento educativo de los padres, las organizaciones representativas de los trabajadores de la educacion y de las instituciones educativas privadas reconocidas oficialmente. h) Cooperar en materia de normativa educacional y mantener vinculos con el Congreso de la Nacion y con las legislaturas de las provincias y de la Municipalidad de la Ciudad de Buenos Aires.


Documento: 10008
Articulo: 10186
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO II: DEL CONSEJO FEDERAL DE CULTURA Y EDUCACION

El Consejo Federal de Cultura y Educacion se compone de los siguientes organos: a) La Asamblea Federal, organo superior del Consejo, estara integrada por el ministro del area del Poder Ejecutivo Nacional como presidente nato, y por los ministros o responsables del Area Educativa de las provincias y la Municipalidad de la Ciudad de Buenos Aires y los representantes del Consejo de Universidades. (Expresion "y el representante del Consejo Interuniversitario Nacional" sustituida por expresion "y los representantes del Consejo de Universidades" por art. 86, inc. c) de la Ley No 24.521 B.O. 10/08/1995). b) El Comite Ejecutivo, desenvolvera sus actividades en el marco de las resoluciones adoptadas por la Asamblea Federal. Estara presidido por el ministro del Poder Ejecutivo Nacional e integrado por los miembros representantes de las regiones que lo componen, designados por la Asamblea Federal cada dos anos. c) La Secretaria General, tendra la mision de conducir y realizar las actividades, trabajos y estudios segun lo establezcan la Asamblea Federal y el Comite Ejecutivo. Su titular sera designado cada dos anos por la Asamblea Federal.


Documento: 10008
Articulo: 10187
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO II: DEL CONSEJO FEDERAL DE CULTURA Y EDUCACION

El Consejo Federal de Cultura y Educacion tendra el apoyo de dos Consejos Consultivos: a) El Consejo Economico-Social, integrado por representantes de las organizaciones gremiales empresarias de la produccion y los servicios, la Confederacion General del Trabajo y el Consejo de Universidades. (Expresion "y el Consejo Interuniversitario Nacional" sustituida por expresion "y el Consejo de Universidades" por art. 86, inc. c) de la Ley No 24.521 B.O. 10/08/1995). b) El Consejo Tecnico-Pedagogico, estara integrado por especialistas designados por miembros del Consejo Federal de Cultura y Educacion (articulo 54) y dos especialistas designados por la organizacion gremial de trabajadores de la educacion de representacion nacional mayoritaria.


Documento: 10008
Articulo: 10188
Capitulo: TITULO X: GOBIERNO Y ADMINISTRACION. CAPITULO III: DE LAS AUTORIDADES JURISDICCIONALES

Las autoridades competentes de las provincias y de la Municipalidad de la Ciudad de Buenos Aires, tienen entre otras las siguientes atribuciones: a) Planificar, organizar y administrar el sistema educativo de su jurisdiccion. b) Aprobar el curriculo de los diversos ciclos, niveles y regimenes especiales en el marco de lo acordado en el Consejo Federal de Cultura y Educacion. c) Organizar y conducir los establecimientos educativos de gestion estatal y autorizar y supervisar los establecimientos de gestion privada en su jurisdiccion. d) Aplicar con las correspondientes adecuaciones, las decisiones del Consejo Federal de Cultura y Educacion. e) Evaluar periodicamente el sistema educativo en el ambito de su competencia, controlando su adecuacion a las necesidades de su comunidad, a la politica educativa nacional y a las politicas y acciones concertadas en el seno del Consejo Federal de Cultura y Educacion, promoviendo la calidad de la ensenanza. f) Promover la participacion de las distintas organizaciones que integren los trabajadores de la educacion, en el mejoramiento de la calidad de la educacion con aportes tecnico-pedagogicos que perfeccionen la practica educativa, como asi tambien la de los otros miembros de la comunidad educativa.


Documento: 10008
Articulo: 10189
Capitulo: TITULO XI: FINANCIAMIENTO

La inversion en el sistema educativo por parte del Estado es prioritaria y se atendera con los recursos que determinen los presupuestos nacional, provinciales y de la Municipalidad de la Ciudad de Buenos Aires, segun corresponda.


Documento: 10008
Articulo: 10190
Capitulo: TITULO XI: FINANCIAMIENTO

La inversion publica consolidada total en educacion (base 1992: 6.120.196.000), sera duplicada gradualmente y como minimo a razon del 20% anual a partir del presupuesto 1993; o se considerara un incremento del 50% en el porcentaje (base 1992: 4%) del Producto Bruto Interno (base 1992: 153.004.900.000), destinado a educacion en 1992. En cualquiera de los dos casos, se considerara a los efectos de la definicion de los montos la cifra que resultare mayor.


Documento: 10008
Articulo: 10191
Capitulo: TITULO XI: FINANCIAMIENTO

La diferencia entre estas metas de cumplimiento obligatorio y los recursos de las fuentes mencionadas en el articulo 60, se financiara con impuestos directos de asignacion especifica aplicados a los sectores de mayor capacidad contributiva.


Documento: 10008
Articulo: 10192
Capitulo: TITULO XI: FINANCIAMIENTO

A los efectos de la implementacion del articulo 61 el Estado nacional, las provincias y la Municipalidad de la Ciudad de Buenos Aires, formalizaran un Pacto Federal Educativo. El mismo sera ratificado por ley del Congreso de la Nacion y por las respectivas legislaturas y considerara como minimo: a) El compromiso de incremento presupuestario educativo anual de cada jurisdiccion. b) El aporte del Estado nacional para el cumplimiento de las nuevas obligaciones que la presente ley determina a las provincias y la Municipalidad de la Ciudad de Buenos Aires. c) La definicion de procedimientos de auditoria eficientes que garanticen la utilizacion de los fondos destinados a educacion en la forma prevista. d) La implementacion de la estructura y objetivos del sistema educativo indicado en la presente ley.


Documento: 10008
Articulo: 10193
Capitulo: TITULO XI: FINANCIAMIENTO

El Poder Ejecutivo nacional financiara total o parcialmente programas especiales de desarrollo educativo que encaren las diversas jurisdicciones con la finalidad de solucionar emergencias educativas, compensar desequilibrios educativos regionales, enfrentar situaciones de marginalidad, o poner en practica experiencias educativas de interes nacional, con fondos que a tal fin le asigne anualmente el presupuesto, o con partidas especiales que se habiliten al efecto.


Documento: 10008
Articulo: 10194
Capitulo: TITULO XI: FINANCIAMIENTO

Las partidas para los servicios asistenciales que se presten en y desde el servicio educativo seran adicionales a las metas establecidas en el articulo 61.


Documento: 10008
Articulo: 10195
Capitulo: TITULO XII: DISPOSICIONES TRANSITORIAS Y COMPLEMENTARIAS

El Ministerio de Cultura y Educacion y las autoridades educativas de las provincias y de la Municipalidad de la Ciudad de Buenos Aires, acordaran en el seno del Consejo Federal de Cultura y Educacion, inmediatamente de producida la promulgacion de la presente ley y en un plazo no mayor a un ano: a) La adecuacion progresiva de la estructura educativa de las jurisdicciones a la indicada por la presente ley, determinando sus ciclos, y los contenidos basicos comunes del nuevo diseno curricular. b) Las modalidades del ciclo Polimodal atendiendo las demandas del campo laboral, las prioridades comunitarias, regionales y nacionales y la necesaria articulacion con la educacion superior. c) La implementacion gradual de la obligatoriedad y la asistencialidad senaladas para los alumnos/as de la Educacion Inicial, la Educacion Especial y la Educacion General Basica y Obligatoria. d) La implementacion de programas de formacion y actualizacion para la docencia que faciliten su adaptacion a las necesidades de la nueva estructura. e) La equivalencia de los titulos docentes y habilitantes actuales en relacion con las acreditaciones que se definan necesarias para la nueva estructura.


Documento: 10008
Articulo: 10196
Capitulo: TITULO XII: DISPOSICIONES TRANSITORIAS Y COMPLEMENTARIAS

El presupuesto de la administracion publica nacional 1993 con destino a las universidades estatales en su conjunto, no sera inferior al Presupuesto 1992, mas la suma anualizada de los incrementos del mencionado ano.


Documento: 10008
Articulo: 10197
Capitulo: TITULO XII: DISPOSICIONES TRANSITORIAS Y COMPLEMENTARIAS

Las disposiciones de esta ley son aplicables a todos los niveles y regimenes especiales educativos con excepcion de las establecidas en los articulos 48, 53, incisos: b, e, i, k, ll, 54 y 56, inciso a) en relacion con las universidades, aspectos que se rigen por la legislacion especifica o la que la reemplace.


Documento: 10008
Articulo: 10198
Capitulo: TITULO XII: DISPOSICIONES TRANSITORIAS Y COMPLEMENTARIAS

Las provincias se abocaran a adecuar su legislacion educativa en consonancia con la presente ley, y a adoptar los sistemas administrativos, de control y de evaluacion, a efectos de facilitar su optima implementacion.


Documento: 10008
Articulo: 10199
Capitulo: TITULO XII: DISPOSICIONES TRANSITORIAS Y COMPLEMENTARIAS

Deroganse todas las disposiciones que se opongan a la presente ley.


Documento: 10008
Articulo: 10200
Capitulo: TITULO XII: DISPOSICIONES TRANSITORIAS Y COMPLEMENTARIAS

Comuniquese al Poder Ejecutivo Nacional.  ALBERTO R. PIERRI.  ORLANDO BRITOS.  Esther H. Pereyra Arandia de Perez Pardo.  Juan Jose Canals. SISTEMA DE PROTECCION INTEGRAL DE LOS DISCAPACITADOS Ley N. 24.314 Accesibilidad de personas con movilidad reducida. Modificacion de la ley N 22.431. Sancionada: Marzo 15 de 1994. Promulgada de hecho: Abril 8 de 1994. El Senado y Camara de Diputados de Nacion Argentina reunidos en Congreso,.sancionan con fuerza de Ley: Accesibilidad de personas con movilidad reducida Modificacion de la ley 22 431 ARTICULO 1o -Sustituyese el capitulo IV y sus articulos componentes 20 21 y 22. por el siguiente texto: CAPITULO IV ACCESIBILIDAD AL MEDIO FISICO Articulo 20-Establecese la prioridad de la supresion de barreras fisicas en los ambitos urbanos arquitectonicos y del transporte que se realicen o en los existentes que remodelen o sustituyan en forma total o parcial sus elementos constitutivos con le fin de lograr la accesibilidad para las personas con movilidad reducida y mediante la aplicacion de las normas contenidas en el presente capitulo.A los fines de la presente ley. entiendese por accesibilidad la posibilidad de las personas con movilidad reducida de gozar de las adecuadas condiciones de seguridad y autonomia como elemento primordial para el desarrollo de las actividades de la vida diaria sin restricciones derivadas del ambito fisico urbano, arquitectonico o del transporte. para su integracion y equiparacion de oportunidades. Entiendese por barreras fisicas urbanas las existentes en las vias y espacios libres publicos a cuya supresion se tendera por el cumplimiento de los siguientes criterios: a) Itinerarios peatonales: contemplaran una anchura minima en todo su recorrido que permita el paso de dos personas,una de ellas en silla de ruedas Los pisos seran antideslizantes sin resaltos ni aberturas que permitan el tropiezo de personas con bastones o sillas de ruedas. Los desniveles de todo tipo tendran un diseno y grado de inclinacion que perrmita la transitabilidad, utilizacion y seguridad de las personas con movilidad reducida: b) Escaleras y rampas: las escaleras deberan ser de escalones cuya dimension vertical y horizontal facilite su utilizacion por personas con movilidad reducida y estaran dotadas de pasamanos Las rampas tendran las caracteristicas senaladas para los desniveles en el apartado a) c)Parques, jardines plazas y espacios libres: deberan observar en sus itinerarios peatonales las normas establecidas para los mismos en el apartado a). Los banos publicos deberan ser accesibles y utilizables por personas de movilidad reducida: d)Estacionamientos: tendran zonas reservadas y senalizadas para vehiculos que transporten personas con movilidad reducida cercanas a los accesos peatonales: e)Senales verticales y elementos urbanos varios: las senales de trafico. semaforos. postes de iluninacion y cualquier otro elemento vertical de senalizacion o de mobiliario urbano se dispondran de forma que no constituyan obstaculos para los no videntes y para las personas que se desplacen en silla de ruedas: f)Obras en la via publica: Estaran senalizadas y protegidas por vallas estables y continuas y luces rojas permanentes, disponiendo los elementos de manera que los no videntes puedan detectar a tiempo la existencia del obstaculo. En las obras que reduzcan la seccion transversal de la acera se debera construir un itinerario peatonal al ternativo con las caracteristicas senaladas en el apartado a) Articulo 21.-Entiendese por barreras arquitectonicas las existentes en los edificios de uso publico sea su propiedad publica o privada. y en los edificios de vivienda: a cuya supresion tendera por la observancia de los criterios contenidos en el presente articulo. Entiendase por adaptabtildad, la posibilidad de modificar en el tiempo el medio fisico con el fin de hacerlo complela y facilmente accesible a las personas con movilidad reducida. Entiendese por practicabilidad la adaptacion limitada a condiciones minimas de los ambitos basicos para ser utilizados por las personas con movilidad reducida.Entiendese por visitabilidad la accesibilidad estrictamente limitada al Ingreso y uso de los espacios comunes y un local sanitario que permita la vida de relacion de las personas con movilidad reducida: a) Edificios de uso publico: deberan observar en general la accesibilidad y posibilidad de uso en todas sus partes por personas de movilidad reducida y en particular la existencia de estacionamientos reservados y senalizados para vehiculos que transporten a dichas personas cercanos a los accesos peatonales; por lo menos un acceso al interior del edificio desprovisto de barreras arquitectonicas espacios de circulacion horizontal que permitan el desplazamiento y maniobra de dichas personas al igual que comunicacion vertical accesible y utilizable por las mismas mediante elementos constructivos o mecanicos y servicios sanitarios adaptados. Los edificios destinados a espectaculos deberan tener zonas reservadas, senalizadas y adaptadas al uso por personas con sillas de ruedas. Los edificios en que se garanticen plenamente las condiciones de accesibilidad ostentaran en su exterior un simbolo indicativo de tal hecho. Las areas sin acceso de publico o las correspondietes a edificios industriales y comerciales tendran los grados de adaptabilidad necesarios para permitir el empleo de personas con movilidad reducida. b) Edificios de viviendas: las viviendas colectivas con ascensor deberan contar con un itinerario practicable por las personas con movilidad reducida, que una la edificacion con la via publica y con las dependencias de uso comun. Asimismo deberan observar en su diseno y ejecucion o en su remodelacion la adaptabilidad a las personas con movilidad reducida en los terminos y grados que establezca la reglamentacion. En materia de diseno y ejecucion o remodelacion de viviendas individuales, los codigos de edificacion han de observar las disposiciones de la presente ley y su reglamentacion. En las viviendas colectivas existentes a la fecha de sancion de la presente ley, deberan desarrollarse condiciones de adaptabiltdad y practicabilidad en los grados y plazos que establezca la reglamentacion. Articulo 22 -Entiendese por barreras en los transportes aquellas existentes en el acceso y utilizacion de los medios de transporte publico terrestres, aereos y acuaticos de corta, rnedia y larga distancia y aquellas que dificulten el uso de medios propios de transporte por las personas con movilidad educida a cuya supresion se tendera por observancia de los sigulentes critertos: a) Vehiculos de transporte publico tendran dos asientos reservados senalizados y cercanos a la puerta por cada coche, para personas con movilidad reducida. Dichas personas estaran autorizadas para descender por cualquiera de las puertas. Los coches contaran con piso antideslizamte y espacio para ubicacion de bastones, muletas, sillas de ruedas y otros elementos de utilizacion por tales personas. En los transportes aereos debera privilegiarse la asignacion de ubicaciones proximas a los accesos para pasajeros con movilidad reducida. Las empresas de transporte colectivo terrestre sometidas al contralor de autoridad acional deberan transportar gratuitamente a las personas con movilidad reducida en el trayecto que medie entre el domicilio de las mismas y el establecimiento educacional y/o de rehabilitacion a los que deban concurrir. La reglamentacion establecera lascomodidades que deben otorgarse a las mismas, las caracteristicas de los pases que deberan exhibir y las sanciones aplicables a los transportistas en caso de inobservancia de esta norma. La franquicia sera extensiva a un acompanante en caso de necesidad documentada. Las empresas de transportes deberan incorporar gradualmente en los plazas y proporciones que establezca la reglamentacion, unidades especialmenle adaptadas para el transporte de personas con movililidad reducida: b)Estaciones de transportes: contemplaran un itinerario peatonal con las caracteristicas senaladas en el articulo 20 apartado a). en toda su extension; bordes de andenes de extura reconocible y antideslizante: paso alternativo a molinetes; les sistema de anuncios por parlantes y servicios sanitarios adaptados. En los aeropuertos se preveran sistemas mecanicos de ascenso y descenso de pasaje con movilidad reducida en el caso que no hubiera metodos alternativos. c) T ransportes propios: las personas con movilidad reducida tendran derecho a libre transito y estacionamiento de acuerdo a lo que establezcan las respectivas disposiciones municipales las que no podran excluir de esas franquicias a los automotores patentados en otras jurisdicciones. Dichas franquicias seran acreditadas por el distintivo de Identificacion a que se refiere el articulo 12 de la ley 19.279. ARTICULO 2o- Agregase al final del articulo 28 de la ley 22 431 el siguiente texto: Las prioridades y plazos de las adecuaciones establecidas en los articulos 20 y 21 relativas a barreras urbanas y en edificios de uso pubilco seran determinadas por la reglamentacion, pero su ejcucion total no podra exceder un plazo de tres (3) anos desde la fecha de sancion de la presente ley. En toda obra nueva o de remodelacion de edificios de vivienda, la aprobacion de los planos requerira imprescindiblemente la inclusion en los mismos de las normas establecidas en el articulo 21 apartado b), su reglamentacion y las respectivas disposiciones municipales en la materia. Las adecuaciones establecidas en el transporte publico por el articulo 22 apartados a) y b) deberan ejecutarse en un plazo maximo de un ano a partir de reglamentada la presente. Su incumplimiento podra determinar la cancelacion del servicio. ARTICULO 3o-Agregese al final del articulo 27 el siguiente texto: Asimismo, se invitara a las provincias a adherir y/o a incorporar en sus respectivas normativas los contenidos de los articulos 20. 21 y 22 de la presente. ARTICULO 4-Deroganse las disposiciones de las leyes 13.512 y 19.279 que se opongan a la presente, asi como toda otra norma a ella contraria. ARTICULO 5o -Comuniquese al Poder Ejecutivo.-ALBERTO R. PIERRI.-CONRADO H. STORANI.-Esther H. Pereyra Arandia de Perez Pardo.-Edgardo Piuzzi.DADA EN LA SALA DE SESIONES DEL CONGRESO ARGENTINO, EN BUENOS AIRES, A LOS QUINCE DIAS DEL MES DE MARZO DEL ANO MIL NOVECIENTOS NOVENTA Y CUATRO.
"""

# Regular expression pattern to match the fields
pattern = r"Documento: (\d+)\nArticulo: (\d+)\nCapitulo: (.+?)\n\n(.+?)(?=\n\nDocumento: |\Z)"

# Find all matches in the text
matches = re.findall(pattern, text, re.DOTALL)

# Construct the JSON object
data = []
for match in matches:
    id = f"{match[0]}-{match[1]}"
    title = match[2].strip()
    context = match[3].strip()
    data.append({
        "id": id,
        "title": title,
        "context": context,
        "question": "",
        "answers": {
            "text": [context],
            "answer_start": [1]
        }
    })

# Convert the data to JSON

# Regular expression pattern to match the fields
pattern = r"Documento: (\d+)\nArticulo: (\d+)\nCapitulo: (.+?)\n\n(.+?)(?=\n\nDocumento: |\Z)"

# Find all matches in the text
matches = re.findall(pattern, text, re.DOTALL)

# Construct the JSON object
data = []
for match in matches:
    id = f"{match[0]}-{match[1]}"
    title = match[2].strip()
    context = match[3].strip()
    data.append({
        "id": id,
        "title": title,
        "context": context,
        "question": "",
        "answers": {
            "text": [context],
            "answer_start": [1]
        }
    })

# Convert the data to JSON
json_data = json.dumps(data, indent=4)

# Write the JSON data to a new file
with open("output.json", "w") as f:
    f.write(json_data)

