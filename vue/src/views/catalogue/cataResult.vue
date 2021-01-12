<template>
  <div class="dormitory" style="margin: 10px 0 0 10px">
    <div>
          <el-card class="box-card">
      <div>
        编目结果:类别-书架号-层数-书册数
      </div>
    </el-card>
    </div>
    <div class="searchWord">
      <div style="display: inline-block">搜索：</div>
      <el-input
        v-model="search"
        style="display: inline-block; width: 1000px"
        placeholder="请输入搜索内容"
      >
      </el-input>
    </div>
    <div class="dormitoryData">
      <el-table
        ref="dormitoryTable"
        :data="tables"
        tooltip-effect="dark"
        stripe
        style="width: 100%"
      >
        <el-table-column type="selection" width="45"></el-table-column>
        <el-table-column label="序号" type="index" width="65"></el-table-column>
        <el-table-column label="ISBN" prop="book_ISBN"> </el-table-column>
        <el-table-column label="书名" prop="book_name"> </el-table-column>
        <el-table-column label="编目号" prop="catalog_id"> </el-table-column>
        <el-table-column label="作者" prop="book_author"> </el-table-column>
        <el-table-column label="出版社" prop="book_public_company">
        </el-table-column>
        <el-table-column label="数量" prop="book_num"> </el-table-column>
        <el-table-column label="操作">
          <template scope="scope">
            <el-button  type="danger" @click="Delete(scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      dormitory: [
        {
          book_ISBN: "987-987-2910-21-1",
          book_name: "大学室友",
          book_author: "测试",
          book_public_company: "测试",
        },
      ],
      search: "",
    };
  },
  computed: {
    // 模糊搜索
    tables() {
      const search = this.search;
      if (search) {
        // filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。
        // 注意： filter() 不会对空数组进行检测。
        // 注意： filter() 不会改变原始数组。
        return this.dormitory.filter((data) => {
          // some() 方法用于检测数组中的元素是否满足指定条件;
          // some() 方法会依次执行数组的每个元素：
          // 如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测;
          // 如果没有满足条件的元素，则返回false。
          // 注意： some() 不会对空数组进行检测。
          // 注意： some() 不会改变原始数组。
          return Object.keys(data).some((key) => {
            // indexOf() 返回某个指定的字符在某个字符串中首次出现的位置，如果没有找到就返回-1；
            // 该方法对大小写敏感！所以之前需要toLowerCase()方法将所有查询到内容变为小写。
            return String(data[key]).toLowerCase().indexOf(search) > -1;
          });
        });
      }
      return this.dormitory;
    },
  },
  created: function () {
    this.getdata();
  },
  mounted: {},
  methods: {
    getdata() {
      let _this = this;
      Axios({
        method: "get",
        url: "/api/catalog/showcatalog",
      }).then(function (res) {
        console.log(res);
        _this.dormitory = res.data.data;
      });
    },
    //删除
    Delete(row) {
      this.$confirm("确定删除此条记录？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          let _this = this;
          let data = new FormData();
          data.append("book_ISBN", row.book_ISBN);
          Axios({
            method: "POST",
            url: "/api/catalog/drop_catalog",
            data: data,
          }).then(function (res) {
            console.log(res);
            if (res.data.status == 0) {
              _this.$message({
                message: res.data.data,
                type: "success",
              });
              _this.getdata();
            } else {
              _this.$message({
                message: res.data.data,
                type: "error",
              });
            }
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style  scoped>
.box-card {
  width: 480px;
}
.el-card {
  text-align: center;
  margin: 0 auto 10px auto;
}
.el-select .el-input {
  width: 191px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}
</style>