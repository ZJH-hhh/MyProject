<template>
    <ContentBase>
        <div class="row">
            <div class="col-4">
                <WorkKind />
            </div>
            <div class="col-8">
                <AllWorkOfSameType />
            </div>
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from './ContentBase.vue';
import WorkKind from './WorkKind.vue';
import AllWorkOfSameType from './AllWorkOfSameType.vue';

export default {
    name: 'IntroduceWork',
    components: {
        ContentBase,
        WorkKind,
        AllWorkOfSameType,
    }
}
</script>

<style scoped></style>