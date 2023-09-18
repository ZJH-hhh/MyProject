<template>
    <div>
        <div style="margin-top: 10px;">
            <el-select v-model="city" clearable placeholder="城市" style="margin: 0px 20px;">
                <el-option v-for="item in cities" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="job" clearable placeholder="岗位">
                <el-option v-for="item in jobs" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-button type="primary" style="margin: 0 20px;" @click="predict()">预测</el-button>
        </div>


        <v-chart class="chart" :option="option" style="margin-top: 10px;" />
    </div>
</template>

<script>
import { timePredict } from '@/api/job.js';

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
import { ref } from 'vue';


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
            city: '',
            job: '',
            cities: [
                {
                    value: '上海',
                    label: '上海',
                },
                {
                    value: '北京',
                    label: '北京',
                },
                {
                    value: '南京',
                    label: '南京',
                },
                {
                    value: '厦门',
                    label: '厦门',
                },
                {
                    value: '天津',
                    label: '天津',
                },
                {
                    value: '广州',
                    label: '广州',
                },
                {
                    value: '成都',
                    label: '成都',
                },
                {
                    value: '杭州',
                    label: '杭州',
                },
                {
                    value: '武汉',
                    label: '武汉',
                },
                {
                    value: '深圳',
                    label: '深圳',
                },
                {
                    value: '西安',
                    label: '西安',
                },
                {
                    value: '重庆',
                    label: '重庆',
                },
            ],
            jobs: [
                {
                    value: '数据分析',
                    label: '数据分析',
                },
                {
                    value: '产品经理',
                    label: '产品经理',
                },
                {
                    value: '前端',
                    label: '前端',
                },
                {
                    value: '后端',
                    label: '后端',
                },
                {
                    value: '项目经理',
                    label: '项目经理',
                },
            ],
            option: {
                title: {
                    text: '薪资预测'
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
        this.predict();
    },
    methods: {
        predict() {
            timePredict(this.city, this.job).then(response => {
                let x = [];
                let y = [];
                response.data.forEach(element => {
                    x.push(element[0]);
                    y.push(element[1]);
                });
                this.option.xAxis.data = x;
                this.option.series[0].data = y;
            })
        },
    }
};
</script>
  
<style scoped>
.chart {
    height: 600px;
}
</style>