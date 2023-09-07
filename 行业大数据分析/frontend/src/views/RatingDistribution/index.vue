<template>
    <v-chart class="chart" :option="option" />
</template>
  
<script>
import { assess } from '@/api/job.js';

import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart, LineChart, BarChart } from "echarts/charts";
import {
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    ToolboxComponent,
    GridComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

import $ from 'jquery';

use([
    CanvasRenderer,
    PieChart,
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    ToolboxComponent,
    GridComponent,
    LineChart,
    BarChart
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
        return {
            option: {
                title: {
                    text: '评分分布情况'
                },
                toolbox: {
                    show: true,
                    feature: {
                        dataZoom: {
                            yAxisIndex: 'none'
                        },
                        dataView: { readOnly: false },
                        magicType: { type: ['line', 'bar'] },
                        restore: {},
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    data: []
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [],
                        type: 'line',
                        smooth: true
                    }
                ]
            }
        };
    },
    mounted() {
        this.getScore();
    },
    methods: {
        getScore() {
            assess().then(response => {
                let x = [];
                let y = [];
                response.data.forEach(element => {
                    x.push(element[0]);
                    y.push(element[1]);
                });
                this.option.xAxis.data = x;
                this.option.series[0].data = y;
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