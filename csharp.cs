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
