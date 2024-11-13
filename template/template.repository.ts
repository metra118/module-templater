import { Repository } from 'typeorm';

import { $$TEMPLATE$$Entity } from './template.entity';

import { CustomRepository } from '~/common/typeorm/custom-typeorm.decorator';

@CustomRepository($$TEMPLATE$$Entity)
export class $$TEMPLATE$$Repository extends Repository<$$TEMPLATE$$Entity> {}
