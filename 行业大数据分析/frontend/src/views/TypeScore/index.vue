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
        const colors = ['#5470C6', '#EE6666'];
        return {
            option: {
                xAxis: {
                    type: 'category',
                    data: [],
                    axisLabel: {
                        rotate: 45, // 设置标签旋转角度为45度
                    },
                },
                yAxis: {
                    type: 'value',
                    min: 6.5
                },
                series: [
                    {
                        data: [],
                        type: 'bar',
                        showBackground: true,
                        backgroundStyle: {
                            color: 'rgba(180, 180, 180, 0.2)'
                        }
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

<!-- <template>
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
</style> -->