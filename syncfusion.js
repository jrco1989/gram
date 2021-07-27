let grid: Grid = new Grid ({
    dataSource: data,
    dataBound: dataBound
    });
function dataBound(args: any): void {
    for (var i = 0; i < this.columns.length; i++) {
        this.columns[0].width = 120;
        if(this.columns[i].field === "OrderDate"){
            this.columns[i].type="date";
        }
        if (this.columns[i].type === "date") {
            this.columns[i].format = { type: "date", format: "dd/MM/yyyy" };
        }
        this.columns[2].format = "P2";
    }
    this.refreshColumns();
}


var aaaa = $("#child1_grid0959").data("ejGrid");
aaaa.hideColumns("VALOR_INCIDENCIA");

var gridObj_DesagregacionesGrid = $("#DesagregacionesGrid").data("ejGrid");