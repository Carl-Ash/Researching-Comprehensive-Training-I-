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
            18: self.return_optimal,
            # 新增的7个扰动方法
            19: self.change_statement_order,
            20: self.move_assignments,
            21: self.div_if_else,
            22: self.div_composed_if,
            23: self.if_continue_to_if_else,
            24: self.extract_if,
            25: self.extract_arithmetic
        }
        self.var_counter = 0
        self.method_counter = 0
        self.used_methods = set()
        self.function_mapping = {}  # 存储函数名映射

    def obfuscate(self, code):
        # 保护特殊占位符 <<$ target $>>
        # 采用严格的行级保护方案，确保包含占位符的行完全不变且保留在原始函数边界内
        lines = code.split('\n')
        protected_lines = []  # 存储被保护行的信息：(原始行号, 原始内容, 缩进级别)
        
        # 第一步：识别并记录所有包含占位符的行及其缩进级别
        for i, line in enumerate(lines):
            if "<<$ target $>>" in line:
                # 计算缩进级别，用于后续确定函数边界
                indent_level = len(line) - len(line.lstrip())
                protected_lines.append((i, line, indent_level))
        
        # 如果没有需要保护的行，直接进行混淆
        if not protected_lines:
            try:
                tree = ast.parse('\n'.join(lines))
                # 预处理：确保所有FunctionDef节点都有lineno和col_offset属性
                class FunctionDefAttributeFixer(ast.NodeTransformer):
                    def visit_FunctionDef(self, node):
                        if not hasattr(node, 'lineno'):
                            node.lineno = 0
                        if not hasattr(node, 'col_offset'):
                            node.col_offset = 0
                        self.generic_visit(node)
                        return node
                tree = FunctionDefAttributeFixer().visit(tree)
                
                # 应用混淆方法
                methods_without_renaming = list(range(1, 26))
                methods_without_renaming.remove(15)  # 移除函数重命名方法
                methods_to_apply = random.sample(methods_without_renaming, min(10, 24))  # 减少应用的方法数量以降低出错风险
                
                for method_id in methods_to_apply:
                    self.used_methods.add(method_id)
                    try:
                        tree = self.apply_method(method_id, tree)
                    except Exception as e:
                        print(f"警告: 应用方法 {method_id} 时出错: {e}")
                        continue
                
                # 最后应用函数重命名方法
                if 15 not in self.used_methods:
                    self.used_methods.add(15)
                    try:
                        tree = self.apply_method(15, tree)
                    except Exception as e:
                        print(f"警告: 应用函数重命名方法时出错: {e}")
                
                # 生成混淆代码并验证
                obfuscated_code = ast.unparse(tree)
                if self.validate_generated_code(obfuscated_code):
                    return obfuscated_code
                else:
                    print("警告: 生成的代码有语法错误，返回原始代码")
                    return code
            except Exception as e:
                print(f"警告: 处理代码时出错: {e}")
                return code
        
        # 分析代码结构，识别函数边界
        class FunctionBoundaryAnalyzer(ast.NodeVisitor):
            def __init__(self):
                self.functions = []  # 存储函数信息：(函数名, 开始行, 结束行)
                
            def visit_FunctionDef(self, node):
                # 记录函数的开始行
                start_line = getattr(node, 'lineno', 0)
                # 估算函数结束行（简化版，实际可能需要更复杂的逻辑）
                end_line = start_line
                # 查找最深的行号
                for child in ast.walk(node):
                    if hasattr(child, 'lineno') and child.lineno > end_line:
                        end_line = child.lineno
                # 增加一些余量
                end_line += 1
                self.functions.append((node.name, start_line, end_line))
                self.generic_visit(node)
        
        try:
            # 尝试解析完整代码以分析函数边界
            original_tree = ast.parse('\n'.join(lines))
            analyzer = FunctionBoundaryAnalyzer()
            analyzer.visit(original_tree)
            function_boundaries = analyzer.functions
        except:
            # 如果解析失败，使用空的函数边界信息
            function_boundaries = []
        
        # 创建一个干净的代码版本，将占位符行替换为特殊标记
        clean_lines = []
        protected_mapping = {}
        for i, line in enumerate(lines):
            if "<<$ target $>>" in line:
                # 生成唯一的行ID，并存储原始行内容
                line_id = f"__PROTECTED_PLACEHOLDER_LINE_{i}__"
                protected_mapping[line_id] = line
                clean_lines.append(f"# {line_id}")  # 用注释标记占位位置
            else:
                clean_lines.append(line)
        
        # 预处理：确保所有FunctionDef节点都有lineno和col_offset属性
        class FunctionDefAttributeFixer(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if not hasattr(node, 'lineno'):
                    node.lineno = 0
                if not hasattr(node, 'col_offset'):
                    node.col_offset = 0
                self.generic_visit(node)
                return node
        
        try:
            # 解析清理后的代码
            clean_code = '\n'.join(clean_lines)
            tree = ast.parse(clean_code)
            tree = FunctionDefAttributeFixer().visit(tree)
            
            # 应用混淆方法，但使用更安全的方法集和更少的方法数量
            # 避免使用可能改变函数边界的方法
            safe_methods = [1, 3, 5, 6, 10, 12, 13, 14, 16, 17, 18, 21, 22, 24, 25]
            methods_to_apply = random.sample(safe_methods, min(8, len(safe_methods)))  # 减少方法数量以降低风险
            
            for method_id in methods_to_apply:
                self.used_methods.add(method_id)
                try:
                    tree = self.apply_method(method_id, tree)
                except Exception as e:
                    print(f"警告: 应用方法 {method_id} 时出错: {e}")
                    continue  # 忽略可能失败的方法
            
            # 如果还没应用函数重命名方法，应用它
            if 15 not in self.used_methods:
                self.used_methods.add(15)
                try:
                    tree = self.apply_method(15, tree)
                except Exception as e:
                    print(f"警告: 应用函数重命名方法时出错: {e}")
            
            # 将混淆后的代码转换回字符串
            obfuscated_code = ast.unparse(tree)
            obfuscated_lines = obfuscated_code.split('\n')
            
            # 重建代码，确保占位符行回到正确位置且保留在原始函数边界内
            final_lines = []
            i = 0  # 原始代码的行索引
            j = 0  # 混淆后代码的行索引
            
            while i < len(lines):
                # 检查当前行是否是需要保护的占位符行
                is_protected = False
                for (orig_line_num, protected_content, _) in protected_lines:
                    if i == orig_line_num:
                        # 这是一个需要保护的占位符行，直接添加原始内容
                        final_lines.append(protected_content)
                        i += 1
                        is_protected = True
                        break
                
                if is_protected:
                    continue
                
                # 对于非占位符行，从混淆后的代码中获取对应行
                if j < len(obfuscated_lines):
                    # 跳过混淆代码中的占位符标记行
                    while j < len(obfuscated_lines):
                        line = obfuscated_lines[j]
                        if any(f"# __PROTECTED_PLACEHOLDER_LINE_{k}__" in line for (k, _, _) in protected_lines):
                            j += 1
                        else:
                            # 确保行不为空且有正确的缩进
                            if line.strip() and ':' in line and 'def ' in line:
                                # 这是一个函数定义行，确保下一行有正确的缩进
                                final_lines.append(line)
                                i += 1
                                j += 1
                                # 检查下一行是否需要添加缩进的pass语句
                                if j < len(obfuscated_lines) and not obfuscated_lines[j].strip():
                                    # 如果下一行是空行，添加一个pass语句
                                    indent = ' ' * (len(line) - len(line.lstrip()))
                                    final_lines.append(f"{indent}pass")
                                    i += 1
                                elif j < len(obfuscated_lines) and len(obfuscated_lines[j].lstrip()) == len(obfuscated_lines[j]):
                                    # 如果下一行没有缩进，添加一个pass语句
                                    indent = ' ' * (len(line) - len(line.lstrip()) + 4)
                                    final_lines.append(f"{indent}pass")
                                    i += 1
                            else:
                                final_lines.append(line)
                                i += 1
                                j += 1
                            break
                else:
                    # 如果混淆后的代码行数不足，使用原始行
                    final_lines.append(lines[i])
                    i += 1
            
            # 构建最终代码
            final_code = '\n'.join(final_lines)
            
            # 确保所有占位符都存在
            for original_line in protected_mapping.values():
                if "<<$ target $>>" not in final_code:
                    # 如果某个占位符丢失，直接添加
                    final_code += '\n' + original_line
            
            # 验证生成的代码
            if self.validate_generated_code(final_code):
                return final_code
            else:
                print("警告: 生成的代码有语法错误，返回修复后的代码")
                # 尝试修复缩进错误
                final_code = self.fix_indentation(final_code)
                if self.validate_generated_code(final_code):
                    return final_code
                else:
                    print("警告: 无法修复代码，返回原始代码")
                    return code
        except Exception as e:
            print(f"警告: 处理带有占位符的代码时出错: {e}")
            return code
            
    def validate_generated_code(self, code):
        """验证生成的代码是否有正确的语法"""
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            print(f"代码语法错误: {e}")
            return False
            
    def fix_indentation(self, code):
        """尝试修复代码中的缩进错误"""
        lines = code.split('\n')
        fixed_lines = []
        current_indent = 0
        indent_size = 4
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # 检查是否是减少缩进的行
            if stripped.startswith('elif') or stripped.startswith('else:') or stripped.startswith('except:') or stripped.startswith('finally:'):
                current_indent = max(0, current_indent - indent_size)
            
            # 应用当前缩进
            if stripped:
                fixed_lines.append(' ' * current_indent + stripped)
            else:
                fixed_lines.append('')
            
            # 检查是否是增加缩进的行
            if stripped.endswith(':'):
                current_indent += indent_size
            
            # 特殊处理函数定义后面的行
            if i < len(lines) - 1 and stripped.startswith('def ') and stripped.endswith(':'):
                next_line = lines[i + 1].strip()
                # 如果函数定义后面没有内容或没有缩进，添加pass语句
                if not next_line or len(lines[i + 1]) == len(next_line):
                    fixed_lines.append(' ' * current_indent + 'pass')
        
        return '\n'.join(fixed_lines)

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
        # 新增的7个方法
        elif method_id == 19:
            return self.change_statement_order(tree)
        elif method_id == 20:
            return self.move_assignments(tree)
        elif method_id == 21:
            return self.div_if_else(tree)
        elif method_id == 22:
            return self.div_composed_if(tree)
        elif method_id == 23:
            return self.if_continue_to_if_else(tree)
        elif method_id == 24:
            return self.extract_if(tree)
        elif method_id == 25:
            return self.extract_arithmetic(tree)
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
            def contains_input_call(self, stmt):
                """检查语句是否包含input函数调用"""
                contains_input = False
                
                class InputCallChecker(ast.NodeVisitor):
                    def __init__(self):
                        self.found = False
                    
                    def visit_Call(self, node):
                        if isinstance(node.func, ast.Name) and node.func.id == 'input':
                            self.found = True
                        self.generic_visit(node)
                
                checker = InputCallChecker()
                checker.visit(stmt)
                return checker.found
            
            def visit_FunctionDef(self, node):
                new_body = []
                for stmt in node.body:
                    new_body.append(stmt)
                    # 随机复制赋值语句，但排除包含input函数调用的语句
                    if (isinstance(stmt, ast.Assign) and 
                        random.random() < 0.3 and 
                        not self.contains_input_call(stmt)):
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
        # 收集所有函数定义，确保递归访问函数体以收集所有函数
        class FunctionCollector(ast.NodeVisitor):
            def __init__(self):
                self.functions = {}
            
            def visit_FunctionDef(self, node):
                old_name = node.name
                new_name = f"obfuscated_func_{random.randint(1000, 9999)}"
                self.functions[old_name] = new_name
                self.generic_visit(node)  # 递归访问函数体以收集内部函数
        
        collector = FunctionCollector()
        collector.visit(tree)
        
        # 同时重命名函数调用和函数定义，确保一致性
        class FunctionRenamer(ast.NodeTransformer):
            def __init__(self, function_mapping):
                self.function_mapping = function_mapping
            
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id in self.function_mapping:
                    node.func.id = self.function_mapping[node.func.id]
                self.generic_visit(node)
                return node
            
            def visit_FunctionDef(self, node):
                if node.name in self.function_mapping:
                    node.name = self.function_mapping[node.name]
                self.generic_visit(node)  # 递归访问函数体以处理内部函数
                return node
        
        if collector.functions:
            # 一次性重命名所有函数调用和定义
            renamer = FunctionRenamer(collector.functions)
            tree = renamer.visit(tree)
        
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

        # 以下是新增的7个扰动方法实现

    def change_statement_order(self, tree):
        """安全版本：不进行语句顺序交换，避免破坏变量依赖关系"""
        class SafeStatementReorder(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                # 不进行任何语句顺序修改，直接返回原始节点
                return node
        
        return SafeStatementReorder().visit(tree)

    def move_assignments(self, tree):
        """修改为安全版本：完全不移动任何赋值语句，避免变量未定义错误"""
        class SafeAssignmentMover(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                # 保持所有语句的原始顺序，不进行任何移动，以避免变量未定义错误
                return node
        return SafeAssignmentMover().visit(tree)

    def div_if_else(self, tree):
        """将If Else-If Else分为If Else If Else"""
        class IfElseDivider(ast.NodeTransformer):
            def visit_If(self, node):
                # 如果有多个elif，将它们转换为嵌套的if-else
                if (node.orelse and len(node.orelse) == 1 and 
                    isinstance(node.orelse[0], ast.If) and 
                    random.random() < 0.5):
                    
                    # 已经是if-elseif结构，保持原样或转换为嵌套
                    current = node
                    while (current.orelse and len(current.orelse) == 1 and 
                           isinstance(current.orelse[0], ast.If)):
                        next_if = current.orelse[0]
                        current.orelse = next_if.body
                        if next_if.orelse:
                            current.orelse.extend(next_if.orelse)
                        current = next_if
                
                return node
        return IfElseDivider().visit(tree)

    def div_composed_if(self, tree):
        """将合成的If语句分成单个语句"""
        class ComposedIfDivider(ast.NodeTransformer):
            def visit_If(self, node):
                if isinstance(node.test, ast.BoolOp) and random.random() < 0.4:
                    # 对于and操作，拆分为嵌套if
                    if isinstance(node.test.op, ast.And):
                        current = node
                        for i, value in enumerate(node.test.values[:-1]):
                            if i == 0:
                                current.test = value
                                new_if = ast.If(
                                    test=node.test.values[i+1],
                                    body=node.body,
                                    orelse=node.orelse
                                )
                                current.body = [new_if]
                                current = new_if
                            else:
                                new_if = ast.If(
                                    test=node.test.values[i+1],
                                    body=node.body,
                                    orelse=node.orelse
                                )
                                current.body = [new_if]
                                current = new_if
                        return node
                    
                    # 对于or操作，拆分为多个if
                    elif isinstance(node.test.op, ast.Or):
                        new_stmts = []
                        for value in node.test.values:
                            new_if = ast.If(
                                test=value,
                                body=node.body,
                                orelse=[]
                            )
                            new_stmts.append(new_if)
                        
                        # 需要在函数级别替换，这里简化处理
                        return node
                
                return node
        return ComposedIfDivider().visit(tree)

    def if_continue_to_if_else(self, tree):
        """将If-Continue语句转换为If-Else语句"""
        class IfContinueConverter(ast.NodeTransformer):
            def visit_While(self, node):
                # 在循环中查找if-continue模式
                self.generic_visit(node)
                return node
            
            def visit_For(self, node):
                # 在循环中查找if-continue模式
                self.generic_visit(node)
                return node
            
            def visit_If(self, node):
                # 检查是否是if-continue模式
                if (len(node.body) == 1 and 
                    isinstance(node.body[0], ast.Continue) and 
                    random.random() < 0.5):
                    
                    # 将if-continue转换为if-else，将原循环体放在else中
                    # 注意：这个转换需要在循环上下文中，这里简化处理
                    if node.orelse:
                        # 如果已经有else，将continue移到else中
                        node.body = node.orelse
                        node.orelse = [ast.Continue()]
                    else:
                        # 如果没有else，创建空的else并交换
                        node.orelse = node.body
                        node.body = [ast.Pass()]
                
                return node
        return IfContinueConverter().visit(tree)

    def extract_if(self, tree):
        """将 if 语句中的条件或代码块提取为独立的方法"""
        class IfExtractor(ast.NodeTransformer):
            def __init__(self, obfuscator):
                self.obfuscator = obfuscator
                self.extracted_functions = []
            
            def collect_variable_names(self, node):
                """收集表达式中使用的变量名"""
                variables = set()
                
                class NameCollector(ast.NodeVisitor):
                    def __init__(self, var_set):
                        self.var_set = var_set
                    
                    def visit_Name(self, node):
                        # 收集加载上下文的变量名（使用的变量）
                        if isinstance(node.ctx, ast.Load):
                            # 排除内置函数和特殊变量
                            if node.id not in ['__name__', '__main__']:
                                self.var_set.add(node.id)
                        self.generic_visit(node)
                
                collector = NameCollector(variables)
                collector.visit(node)
                return variables
            
            def visit_If(self, node):
                # 检查是否是特殊的 __name__ == '__main__' 条件判断
                if (isinstance(node.test, ast.Compare) and 
                    isinstance(node.test.left, ast.Name) and 
                    node.test.left.id == '__name__' and 
                    len(node.test.ops) == 1 and 
                    isinstance(node.test.ops[0], ast.Eq) and 
                    len(node.test.comparators) == 1 and 
                    isinstance(node.test.comparators[0], ast.Constant) and 
                    node.test.comparators[0].value == '__main__'):
                    # 不处理特殊的 __name__ == '__main__' 条件判断
                    return node
                
                if random.random() < 0.3:
                    # 收集条件中使用的变量名
                    used_variables = self.collect_variable_names(node.test)
                    
                    # 提取条件为函数
                    condition_func_name = f"check_condition_{random.randint(100, 999)}"
                    
                    # 创建参数列表
                    args = []
                    for var_name in used_variables:
                        arg = ast.arg(arg=var_name)
                        args.append(arg)
                    
                    # 创建条件函数
                    condition_func = ast.FunctionDef(
                        name=condition_func_name,
                        args=ast.arguments(
                            args=args,
                            posonlyargs=[],
                            kwonlyargs=[],
                            kw_defaults=[],
                            defaults=[]
                        ),
                        body=[ast.Return(value=node.test)],
                        decorator_list=[]
                    )
                    # 确保设置lineno属性，即使原始节点没有这个属性
                    condition_func.lineno = getattr(node, 'lineno', 0)
                    condition_func.col_offset = getattr(node, 'col_offset', 0)
                    
                    # 修改原if语句，传递所有使用的变量作为参数
                    args_to_pass = [ast.Name(id=var_name, ctx=ast.Load()) for var_name in used_variables]
                    node.test = ast.Call(
                        func=ast.Name(id=condition_func_name, ctx=ast.Load()),
                        args=args_to_pass,
                        keywords=[]
                    )
                    
                    self.extracted_functions.append(condition_func)
                return node
            
            def visit_Module(self, node):
                self.extracted_functions = []
                self.generic_visit(node)
                
                # 找到if __name__ == '__main__':语句的位置
                main_block_index = -1
                for i, stmt in enumerate(node.body):
                    if (isinstance(stmt, ast.If) and 
                        isinstance(stmt.test, ast.Compare) and 
                        isinstance(stmt.test.left, ast.Name) and 
                        stmt.test.left.id == '__name__' and 
                        len(stmt.test.ops) == 1 and 
                        isinstance(stmt.test.ops[0], ast.Eq) and 
                        len(stmt.test.comparators) == 1 and 
                        isinstance(stmt.test.comparators[0], ast.Constant) and 
                        stmt.test.comparators[0].value == '__main__'):
                        main_block_index = i
                        break
                
                # 将提取的函数添加到if __name__ == '__main__':语句之前，如果存在的话
                if main_block_index != -1:
                    # 先保存main块
                    main_block = node.body.pop(main_block_index)
                    # 添加提取的函数
                    node.body.extend(self.extracted_functions)
                    # 再添加回main块
                    node.body.append(main_block)
                else:
                    # 如果没有main块，直接添加到末尾
                    node.body.extend(self.extracted_functions)
                
                return node
        
        return IfExtractor(self).visit(tree)

    def extract_arithmetic(self, tree):
        """将算术表达式中的计算部分提取为独立的方法"""
        class ArithmeticExtractor(ast.NodeTransformer):
            def __init__(self, obfuscator):
                self.obfuscator = obfuscator
                self.extracted_functions = []
            
            def collect_variable_names(self, node):
                """收集表达式中使用的变量名"""
                variables = set()
                
                class NameCollector(ast.NodeVisitor):
                    def __init__(self, var_set):
                        self.var_set = var_set
                    
                    def visit_Name(self, node):
                        # 收集加载上下文的变量名（使用的变量）
                        if isinstance(node.ctx, ast.Load):
                            self.var_set.add(node.id)
                        self.generic_visit(node)
                
                collector = NameCollector(variables)
                collector.visit(node)
                return variables
            
            def visit_BinOp(self, node):
                if random.random() < 0.2:
                    # 收集表达式中使用的变量名
                    used_variables = self.collect_variable_names(node)
                    
                    # 提取算术表达式为函数
                    func_name = f"calc_{random.randint(100, 999)}"
                    
                    # 创建参数列表
                    args = []
                    for var_name in used_variables:
                        arg = ast.arg(arg=var_name)
                        args.append(arg)
                    
                    # 创建计算函数
                    calc_func = ast.FunctionDef(
                        name=func_name,
                        args=ast.arguments(
                            args=args,
                            posonlyargs=[],
                            kwonlyargs=[],
                            kw_defaults=[],
                            defaults=[]
                        ),
                        body=[ast.Return(value=node)],
                        decorator_list=[]
                    )
                    # 确保设置lineno和col_offset属性，即使原始节点没有这些属性
                    calc_func.lineno = getattr(node, 'lineno', 0)
                    calc_func.col_offset = getattr(node, 'col_offset', 0)
                    
                    # 替换原表达式，传递所有使用的变量作为参数
                    args_to_pass = [ast.Name(id=var_name, ctx=ast.Load()) for var_name in used_variables]
                    new_node = ast.Call(
                        func=ast.Name(id=func_name, ctx=ast.Load()),
                        args=args_to_pass,
                        keywords=[]
                    )
                    
                    self.extracted_functions.append(calc_func)
                    return new_node
                return node
            
            def visit_Module(self, node):
                self.extracted_functions = []
                self.generic_visit(node)
                
                # 找到if __name__ == '__main__':语句的位置
                main_block_index = -1
                for i, stmt in enumerate(node.body):
                    if (isinstance(stmt, ast.If) and 
                        isinstance(stmt.test, ast.Compare) and 
                        isinstance(stmt.test.left, ast.Name) and 
                        stmt.test.left.id == '__name__' and 
                        len(stmt.test.ops) == 1 and 
                        isinstance(stmt.test.ops[0], ast.Eq) and 
                        len(stmt.test.comparators) == 1 and 
                        isinstance(stmt.test.comparators[0], ast.Constant) and 
                        stmt.test.comparators[0].value == '__main__'):
                        main_block_index = i
                        break
                
                # 将提取的函数添加到if __name__ == '__main__':语句之前，如果存在的话
                if main_block_index != -1:
                    # 先保存main块
                    main_block = node.body.pop(main_block_index)
                    # 添加提取的函数
                    node.body.extend(self.extracted_functions)
                    # 再添加回main块
                    node.body.append(main_block)
                else:
                    # 如果没有main块，直接添加到末尾
                    node.body.extend(self.extracted_functions)
                
                return node
        
        return ArithmeticExtractor(self).visit(tree)



def validate_code(code):
    """验证代码是否可以编译"""
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def main():
    print("=== Python 代码混淆器 ===")
    print("基于25种重构方法进行代码混淆")
    print("支持特殊占位符 <<$ target $>> 保护")
    
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
    # if not validate_code(source_code):
    #     print("警告: 原始代码存在语法错误!")
    #     return
    
    # 获取输出目录
    output_dir = input("请输入输出目录路径 (留空则默认为当前目录下的output): ").strip()
    if not output_dir:
        output_dir = "./output/"
    
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except Exception as e:
            print(f"错误: 无法创建目录 '{output_dir}' - {e}")
            return
    
    # 生成输出文件名
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    
    # 生成3个混淆版本
    for i in range(1, 4):
        print(f"\n生成混淆版本 {i}/3...")
        obfuscator = CodeObfuscator()
        obfuscated_code = obfuscator.obfuscate(source_code)
        
        # 验证混淆后的代码
        # if not validate_code(obfuscated_code):
        #     print(f"警告: 混淆版本 {i} 存在语法错误，跳过保存")
        #     continue
        
        print(f"使用的混淆方法编号: {sorted(obfuscator.used_methods)}")
        
        output_filename = f"{base_name}_obfuscated_v{i}.py"
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(obfuscated_code)
            print(f"混淆后的代码已保存到: {output_path}")
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
            continue
    
    print("\n批量混淆完成!")


if __name__ == "__main__":
    main()



