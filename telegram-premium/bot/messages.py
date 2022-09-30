import abc

import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    """Base messages."""

    @property
    @abc.abstractmethod
    async def start(self) -> str:
        raise NotImplemented

    @property
    @abc.abstractmethod
    async def help(self) -> str:
        raise NotImplemented

    @property
    @abc.abstractmethod
    async def echo(self) -> str:
        raise NotImplemented


class RegularUser(BaseMessages):
    """Messages for regular user."""

    @property
    async def start(self) -> str:
        return 'Привет!'

    @property
    async def help(self) -> str:
        return 'Вам нужно приобрести подписку!'

    @property
    async def echo(self) -> str:
        await update.message.reply_html(
            rf'Hi {user.mention_html()}!',
            reply_markup=tg.ForceReply(selective=True),
        )



