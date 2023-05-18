<template>
    <div class="card">
        <div class="card-body">
            <button @click="init" type="button" class="btn btn-primary btn1">生成数据</button>
            <button @click="update" type="button" class="btn btn-primary btn2">迭代</button>
            <canvas id="myCanvas" width="800" height="500"></canvas>
        </div>
    </div>
</template>

<script>
// import ContentBase from '../components/ContentBase';
import { reactive, ref } from 'vue';

export default {
    name: 'displayPart',
    // components: {
    //     ContentBase,
    // },
    setup(props, context) {
        const circles = reactive({
            circles: []
        });
        let edges = ref([]);
        const radius = 30;
        const colors = reactive(['lightblue', 'lightgreen', 'pink', 'Aqua', 'gray', 'Bisque', 'Coral', 'DarkCyan', 'GreenYellow', 'IndianRed']);

        const init = () => {
            const canvas = document.getElementById('myCanvas');
            const ctx = canvas.getContext('2d');
            // let w = canvas.width;
            // let h = canvas.height;
            // ctx.clearRect(0, 0, canvas.width, canvas.height);
            // console.log(canvas.width, canvas.height);
            // let ctx = canvas.getContext('2d');
            // let ctx = canvas.getContext('2d');
            // 重置渲染上下文并清空画布
            // ctx.setTransform(1, 0, 0, 1, 0, 0);
            ctx.beginPath();
            ctx.fillStyle = "rgba(255,255,255,255)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            // ctx.clearRect(0, 0, canvas.width, canvas.height);

            while (circles.circles.length < 10) {
                let x = Math.random() * (canvas.width - radius * 2) + radius;
                let y = Math.random() * (canvas.height - radius * 2) + radius;

                let flag = false;
                for (let i = 0; i < circles.circles.length; i++) {
                    let other = circles.circles[i];
                    let distance = Math.sqrt((x - other.x) ** 2 + (y - other.y) ** 2);
                    if (distance < radius * 2) {
                        flag = true;
                        break;
                    }
                }

                if (!flag) {
                    let len = circles.circles.length;
                    let color = colors[len];
                    circles.circles.push({ id: len, x: x, y: y, color: color, adjacency: [] });
                }
            }

            let k = 0;
            while (k < 9) {
                let u = Math.floor(Math.random() * 10);
                let v = Math.floor(Math.random() * 10);
                if (u == v) continue;
                if (circles.circles[u].adjacency.includes(v)) continue;
                circles.circles[u].adjacency.push(v);
                circles.circles[v].adjacency.push(u);
                edges.value.push({ u: u, v: v });
                k++;
            }

            draw();
        }

        const check = x => {
            if (circles.circles[x].adjacency.length === 0) return true;
            return false;
        }

        const update = () => {
            let u = Math.floor(Math.random() * 10);

            if (check(u)) return false;

            let mp = new Map();
            let vis = new Set();
            let maxv = 0;
            for (let i = 0; i < circles.circles[u].adjacency.length; i++) {
                let v = circles.circles[u].adjacency[i];
                if (vis.has(v)) continue;
                else vis.add(v);

                let color = circles.circles[v].color;
                if (mp.has(color)) {
                    let old_val = mp.get(color);
                    let new_val = old_val + 1;
                    mp.set(color, new_val);
                }
                else mp.set(color, 1);
                maxv = Math.max(maxv, mp.get(color));
            }

            let tmp = [];
            for (let k of mp.keys()) {
                let v = mp.get(k);
                if (v === maxv) {
                    tmp.push(k);
                }
            }

            let t = Math.floor(Math.random() * tmp.length);
            let change = tmp[t];
            circles.circles[u].color = change;

            let content = '当前迭代的点：' + u;
            context.emit('iteration', content);

            draw();
        }

        const draw = () => {
            const canvas = document.getElementById('myCanvas');
            const ctx = canvas.getContext('2d');
            ctx.beginPath();
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (let i = 0; i < circles.circles.length; i++) {
                let x = circles.circles[i].x, y = circles.circles[i].y;
                let color = circles.circles[i].color;
                ctx.beginPath();
                ctx.arc(x, y, radius, 0, 2 * Math.PI);
                ctx.fillStyle = color;
                ctx.fill();
                ctx.closePath();

                ctx.font = "30px Arial";
                ctx.fillStyle = "#000000";
                ctx.textAlign = "center";
                ctx.textBaseline = "middle";
                ctx.fillText(circles.circles[i].id, x, y);
            }

            for (let i = 0; i < edges.value.length; i++) {
                let u = edges.value[i].u, v = edges.value[i].v;
                let x1 = circles.circles[u].x, y1 = circles.circles[u].y;
                let x2 = circles.circles[v].x, y2 = circles.circles[v].y;

                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.stroke();
            }
        }

        return {
            init,
            update,
        }
    }
}
</script>

<style scoped>
.btn1 {
    float: left;
}

.btn2 {
    float: right;
}
</style>

<style scoped></style>