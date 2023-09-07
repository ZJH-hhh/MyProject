<template>
    <v-chart class="chart" :option="option" />
</template>

<script>
import { cityScore, eduScore } from '@/api/job.js';

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
        const colors = ['#5470C6', '#EE6666'];
        return {
            option: {
                color: colors,
                tooltip: {
                    trigger: 'none',
                    axisPointer: {
                        type: 'cross'
                    }
                },
                legend: {},
                grid: {
                    top: 70,
                    bottom: 50
                },
                xAxis: [
                    {
                        type: 'category',
                        axisTick: {
                            alignWithLabel: true
                        },
                        axisLine: {
                            onZero: false,
                            lineStyle: {
                                color: colors[1]
                            }
                        },
                        axisPointer: {
                            label: {
                                formatter: function (params) {
                                    return (
                                        'Precipitation  ' +
                                        params.value +
                                        (params.seriesData.length ? ': ' + params.seriesData[0].data : '')
                                    );
                                }
                            }
                        },
                        // prettier-ignore
                        data: []
                    },
                    {
                        type: 'category',
                        axisTick: {
                            alignWithLabel: true
                        },
                        axisLine: {
                            onZero: false,
                            lineStyle: {
                                color: colors[0]
                            }
                        },
                        axisPointer: {
                            label: {
                                formatter: function (params) {
                                    return (
                                        'Precipitation  ' +
                                        params.value +
                                        (params.seriesData.length ? '：' + params.seriesData[0].data : '')
                                    );
                                }
                            }
                        },
                        // prettier-ignore
                        data: []
                    }
                ],
                yAxis: [
                    {
                        type: 'value',
                        min: 5
                    }
                ],
                series: [
                    {
                        name: 'Precipitation(2015)',
                        type: 'line',
                        xAxisIndex: 1,
                        smooth: true,
                        emphasis: {
                            focus: 'series'
                        },
                        data: []
                    },
                    {
                        name: 'Precipitation(2016)',
                        type: 'line',
                        smooth: true,
                        emphasis: {
                            focus: 'series'
                        },
                        data: []
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
            cityScore().then(response => {
                console.log(response);
                let x = [];
                let y = [];
                response.data.forEach(element => {
                    x.push(element[0]);
                    y.push(element[1]);
                });
                this.option.xAxis[0].data = x;
                this.option.series[0].data = y;
            })

            eduScore().then(response => {
                console.log(response);
                let x = [];
                let y = [];
                response.data.forEach(element => {
                    x.push(element[0]);
                    y.push(element[1]);
                });
                this.option.xAxis[1].data = x;
                this.option.series[1].data = y;
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