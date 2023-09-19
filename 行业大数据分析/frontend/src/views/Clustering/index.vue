<template>
    <!-- <v-chart class="chart" :option="option" /> -->
    <div id="dom" style="width: 1200px; height: 650px;"></div>
</template>

<script>
import { extendChartView, use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart, LineChart, BarChart, ScatterChart } from "echarts/charts";
import {
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    ToolboxComponent,
    GridComponent,
    VisualMapComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import * as echarts from 'echarts/core';
import { clustering } from '@/api/job.js';

use([
    CanvasRenderer,
    PieChart,
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    ToolboxComponent,
    GridComponent,
    LineChart,
    BarChart,
    ScatterChart,
    VisualMapComponent
]);

export default {
    name: "RatingDistribution",
    components: {
        VChart
    },
    provide: {
        [THEME_KEY]: "vintage"
    },
    data() {
        return {}
    },
    mounted() {
        this.getClustering();
    },
    methods: {
        getClustering() {
            let Dom = document.getElementById('dom');
            this.myChart = echarts.init(Dom);

            let option = {
                tooltip: {
                    trigger: 'item',
                    formatter: '{b}'
                },
                xAxis: {},
                yAxis: {},
                series: [{
                    symbolSize: 5,
                    data: [],
                    type: 'scatter',
                    label: {
                        show: true,
                        position: 'top',
                        formatter: '{b}' // 显示类别名称
                    },
                    itemStyle: {
                        color: function (params) {
                            // 自定义颜色，根据分类属性设置不同颜色
                            var colorMap = {
                                '0': 'blue',
                                '1': 'red',
                                '2': 'green',
                                '3': 'purple',
                                '4': 'orange'
                            };
                            return colorMap[params.data.category];
                        }
                    }
                }]
            };

            clustering().then(response => {
                let data = JSON.parse(response.data);
                data.forEach(element => {
                    option.series[0].data.push({
                        category: element['Cluster'],
                        value: [element['X'], element['Y']]
                    })
                });

                option && this.myChart.setOption(option);
            })
        }
    }
};
</script>

<style scoped>
.chart {
    height: 600px;
}
</style>
