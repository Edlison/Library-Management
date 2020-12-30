<template id='book'>
  <el-table :data="tableData" stripe style="width: 100%">
    <el-table-column prop="Bname" label="书名" width="180"> </el-table-column>
    <el-table-column prop="Bauthor" label="作者" width="180"> </el-table-column>
    <el-table-column prop="Bpub" label="出版社" width="180"> </el-table-column>
    <el-table-column prop="Bnum" label="在馆数量"> </el-table-column>
  </el-table>
</template>

<script>
import { getBook } from '@/api/book'
export default {
  data() {
    return {
      tableData: [
      ],
    };
  },
//  mounted(){
//     //   this.getBook()
//   },
// methods:{
//     //在此处定义方法
//     getBook:function(){
//        ajax({
//         url: "http://127.0.0.1:3000/getbook",
//         type: "post",
//         data: {},
//         dataType: "json",
//         success: function (data) {
//           console.log(data);
//         },
//       })
//     }
//   },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getBook().then(response => {
        this.tableData = response
        console.log(response)
        this.listLoading = false
      })
    }
  }
};
</script>