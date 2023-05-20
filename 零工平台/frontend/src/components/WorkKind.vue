<template>
    <div class="card">
        <div class="card-body" v-for="(item, index) in paginatedData" :key="index">{{ item }}</div>
        <nav aria-label="Page navigation">
            <ul class="pagination">
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                </li>
                <li class="page-item" :class="{ 'active': currentPage === page }" v-for="page in totalPages" :key="page">
                    <a class="page-link" href="#" @click="setCurrentPage(page)">{{ page }}</a>
                </li>
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
import { ref, computed } from 'vue';

export default {
    name: 'WorkKind',
    setup() {
        const currentPage = ref(1);
        const PageSize = 5;
        const data = ref(['技术', '产品', '设计', '运营', '市场', '人力/财务/行政',
            '高级管理', '销售', '传媒', '金融', '教育', '医疗', '贸易', '物流', '旅游']);
        const paginatedData = computed(() => {
            const startIdx = (currentPage.value - 1) * PageSize;
            const endIdx = startIdx + PageSize;
            return data.value.slice(startIdx, endIdx);
        })

        const totalPages = computed(() => {
            // 计算总页数
            return Math.ceil(data.value.length / PageSize);
        });

        const setCurrentPage = page => {
            // 设置当前页码
            currentPage.value = page;
        };

        return {
            currentPage,
            paginatedData,
            totalPages,
            setCurrentPage,
        };
    }
}
</script>

<style scoped>
.card-body {
    height: 45px;
    border-radius: 8px;
}

.card-body:hover {
    box-shadow:
        inset 0 -3em 3em rgba(0, 0, 0, 0.1),
        0 0 0 2px rgb(255, 255, 255),
        0.3em 0.3em 1em;
}

.page-item>a {
    color: #00B4B3;
}

.pagination {
    display: flex;
    justify-content: center;
}

nav {
    margin-top: 10px;
}
</style>