import { Repository } from 'typeorm';

import { TEMPLATEEntity } from './template.entity';

import { CustomRepository } from '~/common/typeorm/custom-typeorm.decorator';

@CustomRepository(TEMPLATEEntity)
export class TEMPLATERepository extends Repository<TEMPLATEEntity> {}
