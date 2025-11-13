import ast
import random
import copy
import os

class CodeObfuscator:
    def __init__(self):
        self.method_map = {
            1: self.api_renaming,
            2: self.arguments_adding,
            3: self.arguments_renaming,
            4: self.dead_for_adding,
            5: self.dead_if_adding,
            6: self.dead_if_else_adding,
            7: self.dead_switch_adding,
            8: self.dead_while_adding,
            9: self.duplication,
            10: self.field_enhancement,
            11: self.for_loop_enhancement,
            12: self.if_enhancement,
            13: self.local_variable_adding,
            14: self.local_variable_renaming,
            15: self.method_name_renaming,
            16: self.plus_zero,
            17: self.print_adding,
            18: self.return_optimal
        }
        self.var_counter = 0
        self.method_counter = 0
        self.used_methods = set()
        self.function_mapping = {}  # 存储函数名映射

    def obfuscate(self, code):
        tree = ast.parse(code)
        # 随机选择几种混淆方法进行应用
        methods_to_apply = random.sample(range(1, 19), random.randint(3, 8))  # 减少混淆方法数量以避免冲突
        for method_id in methods_to_apply:
            self.used_methods.add(method_id)
            # 每个方法单独处理，避免递归问题
            tree = self.apply_method(method_id, tree)
        return ast.unparse(tree)

    def apply_method(self, method_id, tree):
        """单独应用一个混淆方法"""
        if method_id == 1:
            return self.api_renaming(tree)
        elif method_id == 2:
            return self.arguments_adding(tree)
        elif method_id == 3:
            return self.arguments_renaming(tree)
        elif method_id == 4:
            return self.dead_for_adding(tree)
        elif method_id == 5:
            return self.dead_if_adding(tree)
        elif method_id == 6:
            return self.dead_if_else_adding(tree)
        elif method_id == 7:
            return self.dead_switch_adding(tree)
        elif method_id == 8:
            return self.dead_while_adding(tree)
        elif method_id == 9:
            return self.duplication(tree)
        elif method_id == 10:
            return self.field_enhancement(tree)
        elif method_id == 11:
            return self.for_loop_enhancement(tree)
        elif method_id == 12:
            return self.if_enhancement(tree)
        elif method_id == 13:
            return self.local_variable_adding(tree)
        elif method_id == 14:
            return self.local_variable_renaming(tree)
        elif method_id == 15:
            return self.method_name_renaming(tree)
        elif method_id == 16:
            return self.plus_zero(tree)
        elif method_id == 17:
            return self.print_adding(tree)
        elif method_id == 18:
            return self.return_optimal(tree)
        return tree

    def api_renaming(self, tree):
        # 由于Python动态特性，API重命名较难实现，这里跳过
        return tree

    def arguments_adding(self, tree):
        # 这个方法容易导致函数调用错误，暂时跳过
        return tree

    def arguments_renaming(self, tree):
        # 这个方法容易导致变量作用域问题，暂时跳过
        return tree

    def dead_for_adding(self, tree):
        class DeadForAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.5:
                    dead_for = ast.For(
                        target=ast.Name(id="_", ctx=ast.Store()),
                        iter=ast.Call(
                            func=ast.Name(id="range", ctx=ast.Load()),
                            args=[ast.Constant(value=0)],
                            keywords=[]
                        ),
                        body=[ast.Pass()],
                        orelse=[]
                    )
                    # 设置lineno以避免错误
                    if hasattr(node, 'lineno'):
                        dead_for.lineno = node.lineno
                    node.body.insert(0, dead_for)
                return node
        return DeadForAdder().visit(tree)

    def dead_if_adding(self, tree):
        class DeadIfAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.5:
                    dead_if = ast.If(
                        test=ast.Constant(value=False),
                        body=[ast.Pass()],
                        orelse=[]
                    )
                    if hasattr(node, 'lineno'):
                        dead_if.lineno = node.lineno
                    node.body.insert(0, dead_if)
                return node
        return DeadIfAdder().visit(tree)

    def dead_if_else_adding(self, tree):
        class DeadIfElseAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.5:
                    dead_if_else = ast.If(
                        test=ast.Constant(value=False),
                        body=[ast.Pass()],
                        orelse=[ast.Pass()]
                    )
                    if hasattr(node, 'lineno'):
                        dead_if_else.lineno = node.lineno
                    node.body.insert(0, dead_if_else)
                return node
        return DeadIfElseAdder().visit(tree)

    def dead_switch_adding(self, tree):
        # Python没有switch，使用match-case (Python 3.10+)
        class DeadSwitchAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.5:
                    dead_match = ast.Match(
                        subject=ast.Constant(value=0),
                        cases=[
                            ast.match_case(
                                pattern=ast.Constant(value=1),
                                body=[ast.Pass()]
                            ),
                            ast.match_case(
                                pattern=ast.MatchValue(value=ast.Constant(value=0)),
                                body=[ast.Pass()]
                            )
                        ]
                    )
                    if hasattr(node, 'lineno'):
                        dead_match.lineno = node.lineno
                    node.body.insert(0, dead_match)
                return node
        return DeadSwitchAdder().visit(tree)

    def dead_while_adding(self, tree):
        class DeadWhileAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.5:
                    dead_while = ast.While(
                        test=ast.Constant(value=False),
                        body=[ast.Pass()],
                        orelse=[]
                    )
                    if hasattr(node, 'lineno'):
                        dead_while.lineno = node.lineno
                    node.body.insert(0, dead_while)
                return node
        return DeadWhileAdder().visit(tree)

    def duplication(self, tree):
        class Duplicator(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                new_body = []
                for stmt in node.body:
                    new_body.append(stmt)
                    # 随机复制赋值语句
                    if isinstance(stmt, ast.Assign) and random.random() < 0.3:
                        new_stmt = copy.deepcopy(stmt)
                        if hasattr(stmt, 'lineno'):
                            new_stmt.lineno = stmt.lineno
                        new_body.append(new_stmt)
                node.body = new_body
                return node
        return Duplicator().visit(tree)

    def field_enhancement(self, tree):
        class FieldEnhancer(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                # 为参数添加None检查
                for arg in node.args.args:
                    check_if = ast.If(
                        test=ast.Compare(
                            left=ast.Name(id=arg.arg, ctx=ast.Load()),
                            ops=[ast.Is()],
                            comparators=[ast.Constant(value=None)]
                        ),
                        body=[ast.Expr(value=ast.Call(
                            func=ast.Name(id="print", ctx=ast.Load()),
                            args=[ast.Constant(value=f"Parameter {arg.arg} is None")],
                            keywords=[]
                        ))],
                        orelse=[]
                    )
                    if hasattr(node, 'lineno'):
                        check_if.lineno = node.lineno
                    node.body.insert(0, check_if)
                return node
        return FieldEnhancer().visit(tree)

    def for_loop_enhancement(self, tree):
        class ForLoopEnhancer(ast.NodeTransformer):
            def visit_For(self, node):
                # 将range(10) -> range(0, 10)
                if isinstance(node.iter, ast.Call) and \
                   isinstance(node.iter.func, ast.Name) and \
                   node.iter.func.id == "range":
                    if len(node.iter.args) == 1:
                        node.iter.args = [ast.Constant(value=0), node.iter.args[0]]
                return node
        return ForLoopEnhancer().visit(tree)

    def if_enhancement(self, tree):
        class IfEnhancer(ast.NodeTransformer):
            def visit_If(self, node):
                # 将if True -> if (1==1)
                if isinstance(node.test, ast.Constant) and node.test.value is True:
                    node.test = ast.Compare(
                        left=ast.Constant(value=1),
                        ops=[ast.Eq()],
                        comparators=[ast.Constant(value=1)]
                    )
                elif isinstance(node.test, ast.Constant) and node.test.value is False:
                    node.test = ast.Compare(
                        left=ast.Constant(value=1),
                        ops=[ast.Eq()],
                        comparators=[ast.Constant(value=0)]
                    )
                return node
        return IfEnhancer().visit(tree)

    def local_variable_adding(self, tree):
        class LocalVarAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.5:
                    new_var = ast.Assign(
                        targets=[ast.Name(id=f"__temp_var_{random.randint(100, 999)}", ctx=ast.Store())],
                        value=ast.Constant(value=random.randint(0, 100))
                    )
                    if hasattr(node, 'lineno'):
                        new_var.lineno = node.lineno
                    node.body.insert(0, new_var)
                return node
        return LocalVarAdder().visit(tree)

    def local_variable_renaming(self, tree):
        # 这个方法容易导致变量作用域问题，暂时跳过
        return tree

    def method_name_renaming(self, tree):
        # 收集所有函数定义
        class FunctionCollector(ast.NodeVisitor):
            def __init__(self):
                self.functions = {}
            
            def visit_FunctionDef(self, node):
                old_name = node.name
                new_name = f"obfuscated_func_{random.randint(1000, 9999)}"
                self.functions[old_name] = new_name
                self.generic_visit(node)
        
        collector = FunctionCollector()
        collector.visit(tree)
        
        # 重命名函数定义和调用
        class MethodRenamer(ast.NodeTransformer):
            def __init__(self, function_mapping):
                self.function_mapping = function_mapping
            
            def visit_FunctionDef(self, node):
                if node.name in self.function_mapping:
                    node.name = self.function_mapping[node.name]
                return node
            
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id in self.function_mapping:
                    node.func.id = self.function_mapping[node.func.id]
                return node
        
        if collector.functions:
            renamer = MethodRenamer(collector.functions)
            return renamer.visit(tree)
        return tree

    def plus_zero(self, tree):
        class PlusZeroAdder(ast.NodeTransformer):
            def visit_Assign(self, node):
                if isinstance(node.value, ast.Constant) and isinstance(node.value.value, (int, float)):
                    if random.random() < 0.5:
                        node.value = ast.BinOp(
                            left=node.value,
                            op=ast.Add(),
                            right=ast.Constant(value=0)
                        )
                return node
        return PlusZeroAdder().visit(tree)

    def print_adding(self, tree):
        class PrintAdder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if random.random() < 0.3:
                    print_stmt = ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id="print", ctx=ast.Load()),
                            args=[ast.Constant(value=f"Debug: {random.randint(1, 100)}")],
                            keywords=[]
                        )
                    )
                    if hasattr(node, 'lineno'):
                        print_stmt.lineno = node.lineno
                    node.body.insert(random.randint(0, len(node.body)), print_stmt)
                return node
        return PrintAdder().visit(tree)

    def return_optimal(self, tree):
        class ReturnOptimizer(ast.NodeTransformer):
            def visit_Return(self, node):
                # 将 return x -> return x if True else None
                if node.value is not None:
                    node.value = ast.IfExp(
                        test=ast.Constant(value=True),
                        body=node.value,
                        orelse=ast.Constant(value=None)
                    )
                return node
        return ReturnOptimizer().visit(tree)


def validate_code(code):
    """验证代码是否可以编译"""
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def main():
    print("=== Python 代码混淆器 ===")
    print("基于18种重构方法进行代码混淆")
    
    # 获取输入文件路径
    input_path = input("请输入要混淆的Python文件路径: ").strip()
    if not os.path.exists(input_path):
        print(f"错误: 文件 '{input_path}' 不存在!")
        return
    
    # 读取源代码
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except Exception as e:
        print(f"错误: 无法读取文件 '{input_path}' - {e}")
        return
    
    print(f"\n读取的原始代码 ({len(source_code)} 字符):")
    print(source_code[:500] + ("..." if len(source_code) > 500 else ""))
    
    # 验证原始代码
    if not validate_code(source_code):
        print("警告: 原始代码存在语法错误!")
        return
    
    obfuscator = CodeObfuscator()
    obfuscated_code = obfuscator.obfuscate(source_code)
    
    # 验证混淆后的代码
    if not validate_code(obfuscated_code):
        print("警告: 混淆后的代码存在语法错误!")
        return
    
    print(f"\n使用的混淆方法编号: {sorted(obfuscator.used_methods)}")
    
    # 获取输出文件路径
    output_dir = input("请输入输出目录路径 (留空则默认为当前目录下的base/output): ").strip()
    if not output_dir:
        output_dir = "./base/output/"
    
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except Exception as e:
            print(f"错误: 无法创建目录 '{output_dir}' - {e}")
            return
    
    # 生成输出文件名
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_filename = f"{base_name}_obfuscated.py"
    output_path = os.path.join(output_dir, output_filename)
    
    # 写入混淆后的代码
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        print(f"\n混淆后的代码已保存到: {output_path}")
        print(f"文件大小: {len(obfuscated_code)} 字符")
        
        # 验证保存的代码
        with open(output_path, 'r', encoding='utf-8') as f:
            saved_code = f.read()
        if validate_code(saved_code):
            print("✓ 保存的代码语法正确")
        else:
            print("✗ 保存的代码存在语法错误")
            
    except Exception as e:
        print(f"错误: 无法写入文件 '{output_path}' - {e}")
        return
    
    # 询问是否显示混淆后的代码
    show_code = input("是否显示混淆后的代码? (y/n): ").strip().lower()
    if show_code == 'y':
        print("\n混淆后的代码:")
        print(obfuscated_code)


if __name__ == "__main__":
    main()



