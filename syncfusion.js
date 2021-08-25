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


$("#CANTIDAD_APU_ITEM").ejNumericTextbox({
    incrementStep: 0.001,
    width: "100%",
    decimalPlaces: 4,
    showRoundedCorner: true,
    minValue: 0,
    value: cantidad_agrupada,
    enabled: item_editable_popUP,
    //change : 'function'
    change: function (args) {
        var nuevo_valor_total = document.getElementById("VALOR_UNITARIO_APU_ITEM").value * args.value;
        let objetoVALOR_TOTAL_APU_ITEM = $("#VALOR_TOTAL_APU_ITEM").data('ejCurrencyTextbox')
        objetoVALOR_TOTAL_APU_ITEM.option("value", nuevo_valor_total)
    },
});