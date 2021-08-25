//string str = amount.ToString("0.00")
var item_contrato_orden = db.VISTA_CONTRATO_ITEMS_ORDEN_M.FirstOrDefault(o => o.COD_ITEM == cod_item);
var item_contrato = db.CONTRATOS_ITEM.SingleOrDefault(o => o.COD_ITEM == cod_item);
var item_contrato_orden = db.VISTA_CONTRATO_ITEMS_ORDEN_M.Where(o => o.COD_ITEM == cod_item).OrderByDescending(q => q.COD_ORDEN_PAGO).FirstOrDefault();
IEnumerable DataSource = db.PROYECTOS.Where(proyecto=> cod_proyectos_usuario.Any(proyecto_de_usuario => proyecto.COD_PROYECTO == proyecto_de_usuario)).ToList();

db.CONTRATOS.Single(p => p.COD_CONTRATO == cod_contrato).USA_TASKGO;
db.ORDENES_PAGO.Where(x => x.COD_CONTRATO == Cn && x.NUMERO_ORDEN == Num).ToList()

VISTA_CANTIDAD_APROBADA_ITEM_M item_cantidad_aprobada = new VISTA_CANTIDAD_APROBADA_ITEM_M();
return Json(new { cantidad_max = cantidad_max, cantidad_disponible = cantidad_disponible.ToString() }, JsonRequestBehavior.AllowGet);

if(revision_obra==true ||  contrato.USA_TASKGO==true)
{
    ver_soportes_revision = true;
}
if(revision_obra==true && contrato.USA_TASKGO==true)
{
    ver_soportes_revision = true;
}

var revision_obra = db.PROYECTOS.Single(p => p.COD_PROYECTO == contrato.COD_PROYECTO).REVISION_OBRA;
try
{
    var numero = db.ORDENES_PAGO.Where(x => x.COD_CONTRATO == Cn && x.NUMERO_ORDEN == Num).ToList();
if (numero.Count() > 0)
{
    return Content("error");
}
else
{
    ORDENES_PAGO updatedOp = db.ORDENES_PAGO.Find(Op);
    db.SaveChanges();
    return Content("ok");
}
}
catch
{                
}
