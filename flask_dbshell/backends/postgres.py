from . import BaseBackend


class PostgresBackend(BaseBackend):

    def compile_command(self):
        cmd = 'postgres://'
        if self._dburl.user:
            cmd += self._dburl.user
        if self._dburl.password:
            cmd += ':%s' % self._dburl.password
        if self._dburl.host:
            cmd += '@%s' % self._dburl.host
        if self._dburl.port:
            cmd += ':%s' % self._dburl.port
        if self._dburl.database is not None:
            cmd += '/%s' % self._dburl.database

        return ['psql', cmd]
