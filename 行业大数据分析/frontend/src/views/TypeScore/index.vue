<template>
    <v-chart class="chart" :option="option" />
</template>
  
<script>
import { typeScore } from '@/api/job.js';

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
                    text: '岗位评分 TOP 10'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: 'bottom'
                },
                toolbox: {
                    show: true,
                    feature: {
                        mark: { show: true },
                        dataView: { show: true, readOnly: false },
                        restore: { show: true },
                        saveAsImage: { show: true }
                    }
                },
                series: [
                    {
                        name: 'Nightingale Chart',
                        type: 'pie',
                        radius: [50, 250],
                        center: ['50%', '50%'],
                        roseType: 'area',
                        itemStyle: {
                            borderRadius: 8
                        },
                        data: [],
                    }
                ]
            }
        };
    },
    mounted() {
        this.getTypeScore();
    },
    methods: {
        getTypeScore() {
            typeScore().then(response => {
                console.log(response);
                response.data.forEach(element => {
                    this.option.series[0].data.push({ name: element[0], value: element[1] });
                });
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