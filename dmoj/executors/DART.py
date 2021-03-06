from .base_executor import ScriptExecutor


class Executor(ScriptExecutor):
    ext = '.dart'
    name = 'DART'
    nproc = -1  # Dart uses a really, really large number of threads
    command = 'dart'
    test_program = '''
void main() {
    print("echo: Hello, World!");
}
'''
    address_grace = 786432

    syscalls = ['epoll_create', 'epoll_ctl', 'epoll_wait', 'restart_syscall',
                'timerfd_settime', 'pipe2',
                ('write', lambda debugger: debugger.uarg0 <= 4)]

    fs = ['/proc/meminfo$', '/proc/sys/vm/overcommit_memory$', '.*/vm-service$']

